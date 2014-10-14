from __future__ import division

from nodeselection import nodeselection
from draw.draw import draw

import logging
import random
import time
import datetime

from numpy import linalg , mean , sqrt
from multiprocessing import Pool
from os.path import join


class training():

    ##define the configuration

    def __init__(self , config):

        self.logger = logging.getLogger('sublog')
        self.config_f = config
        self.mainSampleDict = self.config_f.mainSampleDict
        self.mainNodesDict = self.config_f.mainNodesDict
        self.draw_f = draw(self.mainNodesDict , self.mainSampleDict , self.config_f)

        self.LinearRadiusGradient = (1 - self.config_f.effRadius) / (0.8*self.config_f.maxTrainingIteration)

        if self.config_f.nodesWidth <= self.config_f.nodesHeight:
            self.config_f.effRadius = self.config_f.initialRadius * self.config_f.nodesWidth
        else:
            self.config_f.effRadius = self.config_f.initialRadius * self.config_f.nodesHeight


    def changeWeightVector(self , affectedNode_l, selectedNode_id, sampleNode_id, radius):

        sampleWightVector = self.mainSampleDict[sampleNode_id]['vector']
        self.mainNodesDict[selectedNode_id]['vector'] = sampleWightVector

        #changing affected nodes

        def pertubationThis_m(node):

            nodeDistance = linalg.norm(self.mainNodesDict[selectedNode_id]['position'] - self.mainNodesDict[node]['position'])
            distanceDecay = (radius - nodeDistance) / radius
            affectingWeight = self.mainSampleDict[sampleNode_id]['vector'] - self.mainNodesDict[selectedNode_id]['vector']
            self.mainNodesDict[node]['vector'] = self.mainNodesDict[node]['vector'] + distanceDecay*affectingWeight
            self.mainNodesDict[node]['label'] = 'Empty'

        map(pertubationThis_m , affectedNode_l)

    def giveElipseRadius(self , perceentageDiff):

        radius = self.frontConst*sqrt(abs(self.initialPercentageDiffSqr - perceentageDiff*perceentageDiff)) - (self.config_f.effRadius + 1)
        radius = abs(radius)
        return radius

    def giveLinerRadius(self , irr):

        return self.LinearRadiusGradient * irr + self.config_f.effRadius

    def givePercentageDiff_m(self, sample_id):
        smallestDiffNode_id , diff  = self.nodeselection_f.giveSmallest(sample_id)
        nodeVectorWeight = linalg.norm(self.mainNodesDict[smallestDiffNode_id]['vector'])
        return abs(diff / nodeVectorWeight)

    def start(self):

        #checking whether the mainSampleDict and mainNodeDict is None or not
        if hasattr(self.config_f, 'mainSampleDict') and self.config_f.mainSampleDict != None \
            and hasattr(self.config_f, 'mainNodeDict' ) and self.config_f.mainSampleDict != None:

            self.nodeselection_f = nodeselection(mainNodesDict= self.mainNodesDict , mainSampleDict= self.mainSampleDict)

        else:
            raise Exception('mainSampleDict or mainNodeDict is None')


        #calculating initial Percentage Diff
        self.logger.info('Calculating initial percentage diff between sample and node weight vector')

        sampleSize = int(0.8 * len(self.mainSampleDict))
        #the old has scalling problem and its to slow. since self.mainSampleDict.keys() is a integer, then we cheat a bit
        #sampleId_l = [random.choice(self.mainSampleDict.keys()) for i in range(sampleSize)]
        sampleLenght = int(len(self.mainSampleDict)-1)
        sampleId_l = [random.randint(0 , sampleLenght) for i in range(sampleSize)]

        pool_f = Pool()
        #percentageDiff_l = pool_f.map(self.givePercentageDiff_m , sampleId_l)
        percentageDiff_l = map(self.givePercentageDiff_m , sampleId_l)

        self.initialPercentageDiff = mean(percentageDiff_l)
        self.logger.info('Initial Percentage Vector Weight Diff:%s ' % self.initialPercentageDiff *100 )
        self.initialPercentageDiffSqr = self.initialPercentageDiff*self.initialPercentageDiff
        self.frontConst = (self.config_f.effRadius + 1)/self.initialPercentageDiff

        irr = 0
        meanPercentageDiff = 9999
        percentageDiff_l = []

        trainingOutputFile = join(self.config_f.projectDirectory, datetime.datetime.now().strftime('%Y_%m_%d_%H%M%S_trainingOutput.txt'))
        trainingOutput_F = open(trainingOutputFile , 'w')
        trainingOutput_F.write('Iteration\tPercentage Difference\tRadius\n')

        while irr <= self.config_f.maxTrainingIteration and meanPercentageDiff > self.config_f.minPercentDiffToStopTrain and trainingOutput_F:

            # pick randomly sample
            sample_id = random.randint(0 , len(self.mainSampleDict)-1)
            sampleVectorWeight = linalg.norm(self.mainSampleDict[sample_id]['vector'])

            #node with the smallest diff
            smallestDiffNode_id , diff  = self.nodeselection_f.giveSmallest(sample_id)
            percentageDiff = diff / sampleVectorWeight
            percentageDiff = abs(percentageDiff)
            percentageDiff_l.append(percentageDiff)

            #calculate the radius
            #radius = self.giveElipseRadius(percentageDiff)
            radius = self.giveLinerRadius(irr)

            #change the selectNode with the smallest diff
            self.mainNodesDict[smallestDiffNode_id]['vector'] = self.mainSampleDict[sample_id]['vector']
            self.mainNodesDict[smallestDiffNode_id]['label'] = self.mainSampleDict[sample_id]['label']

            #affected nodes
            affectedNodes_l = self.nodeselection_f.giveNodeInRadius(smallestDiffNode_id,radius)
            #changing the neighbour vector weight
            if radius > 1:
                self.changeWeightVector(affectedNodes_l, smallestDiffNode_id , sample_id , radius)
            percentageDiff = percentageDiff * 100
            self.logger.info('Iteration:%s, Percentage Differences:%.3f ,Radius:%s' % (irr, percentageDiff , radius))
            trainingOutput_F.write('%s,\t%.3f,\t%s\n' % (irr, percentageDiff , radius))

            #sleep function
            if irr % self.config_f.sleepAtIteration == 0:
                if irr != 0:
                    meanPercentageDiff = mean(percentageDiff_l)
                    percentageDiff_l=[]

                self.draw_f.textDrawMainNodes()
            irr += 1

        trainingOutput_F.close()
