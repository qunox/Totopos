from __future__ import  division
import random
import logging

from numpy import array

__author__ = 'qunox'

class blob():

    def __init__(self, maxpoint):

        self.logger = logging.getLogger('sublog')

        self.maxPoint = maxpoint
        self.blobA = {'label' : 'A' , 'center' : [1,5,7] , 'radius' : 3.0 , 'pointlist' : []}
        self.blobB = {'label' : 'B' , 'center' : [10,5,17] , 'radius' : 5.0 , 'pointlist' : []}
        self.blobC = {'label' : 'C' , 'center' : [17,25,-7] , 'radius' : 1.5 , 'pointlist' : []}
        self.blobD = {'label' : 'D' , 'center' : [12,-5,45] , 'radius' : 9.0 , 'pointlist' : []}

        self.completeBlob = [ self.blobA , self.blobB , self.blobC , self.blobD]
        self.logger.debug('Blob origin: %s' %self.completeBlob)

    def populateBlob(self):

        sample_dict = {}

        for blob in self.completeBlob:

            point = blob['center']
            dimensionPoint_L = []
            for dimension in point:

                limit1 = int(dimension + blob['radius'])
                limit2 = int(dimension - blob['radius'])

                if limit1 < limit2 :
                    left = limit1
                    right = limit2
                else:
                    left = limit2
                    right = limit1

                dimension_L = [random.randint(left, right) for i in range(self.maxPoint)]
                dimensionPoint_L.append(dimension_L)

            point_L = []

            for i in range(self.maxPoint):
                aPoint = []
                for dimension in dimensionPoint_L:
                    aPoint.append(dimension[i])
                point_L.append(aPoint)

            i = 0
            for aPoint in point_L:
                sample_dict[i] = {'vector' : array(aPoint) , 'label': blob['label']}
                i +=1

        self.logger.debug('Full list of sample:\n%s' % sample_dict)
        return sample_dict


