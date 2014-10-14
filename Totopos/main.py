from __future__ import division

import sys
import logging
import datetime
import os
import multiprocessing

from sample.blob import blob
from sample.targetted import targetted
from node.shape import shape
from node.vectoroperation import vectoroperation
from training.training import training

__author__ = 'qunox'


'''_____               _                _
  / ____|             | |              | |
 | |      ___   _ __  | |_  _ __  ___  | |
 | |     / _ \ | '_ \ | __|| '__|/ _ \ | |
 | |____| (_) || | | || |_ | |  | (_) || |
  \_____|\___/ |_| |_| \__||_|   \___/ |_|
'''

class config():

    def __init__(self):

        self.mainSampleDict = None
        self.mainNodeDict = None
        self.initialRadius = 0.9
        self.minPercentDiffToStopTrain = 0.001
        self.maxTrainingIteration = 100000

        self.sleepAtIteration = 10000
        self.decayRate = (self.maxTrainingIteration - 0.1*self.maxTrainingIteration) / 100

        #General
        self.projectDirectory = os.getcwd()

        #Logging
        self.loggerLevel = logging.DEBUG

        #Sample
        self.maxSamplePoint = 250

        #nodes
        self.nodesShape = 'rectangular'
        self.nodesWidth = 100
        self.nodesHeight = 100

        self.proccessPoolNumber = multiprocessing.cpu_count()



if __name__ == '__main__':

    config_f = config()
    '''
     | |
     | |      ___    __ _
     | |     / _ \  / _` |
     | |____| (_) || (_| |
     |______|\___/  \__, |
                     __/ |
                    |___/
    '''

    outputFile_path = config_f.projectDirectory + datetime.datetime.now().strftime('%Y_%m_%d_SOM')
    config_f.projectDirectory = outputFile_path

    if not os.path.exists(outputFile_path):
        os.makedirs(outputFile_path)

    print '...Setting up logger'

    logger = logging.getLogger('sublog')
    logger.setLevel(config_f.loggerLevel)

    #Setting up a console logger
    consoleHandler = logging.StreamHandler(sys.stdout)
    consoleHandler.setFormatter(logging.Formatter('%(message)s'))
    consoleHandler.setLevel(logging.INFO)
    logger.addHandler(consoleHandler)

    #setting up a file logger
    fileHandler = logging.FileHandler(outputFile_path+'/main.log')
    fileHandler.setFormatter(logging.Formatter("%(levelname)s %(asctime)s %(module)s: \t %(message)s"))
    fileHandler.setLevel(logging.DEBUG)
    logger.addHandler(fileHandler)

    logger.info('Finish setting up the log')
    logger.debug('\n\n>>>> START LOG <<<<\n')
    '''                        _
                              | |
     ___  __ _ _ __ ___  _ __ | | ___
    / __|/ _` | '_ ` _ \| '_ \| |/ _ \
    \__ | (_| | | | | | | |_) | |  __/
    |___/\__,_|_| |_| |_| .__/|_|\___|
                        | |
                        |_|

    logger.info('Creating sample: Targetted type')
    blob_f = blob(config_f.maxSamplePoint)
    mainSample_dict = blob_f.populateBlob()
    config_f.mainSampleDict = mainSample_dict
    logger.info('Number of item in sample: %s' % len(mainSample_dict))
    logger.info('Finish creating sample')
    '''
    logger.info('Creating sample: Targeted type')
    targetted_f = targetted()
    mainSample_dict = targetted_f.giveSample()
    config_f.mainSampleDict = mainSample_dict
    logger.info('Number of item in sample: %s' % len(mainSample_dict))
    logger.info('Finish creating sample')


    '''              _
                    | |
     _ __   ___   __| | ___
    | '_ \ / _ \ / _` |/ _ \
    | | | | (_) | (_| |  __/
    |_| |_|\___/ \__,_|\___|
    '''

    shape_f = shape()
    logger.info('Creating nodes')
    logger.info('Shape: %s\tWidth: %s\tHeight: %s' %(config_f.nodesShape, config_f.nodesWidth, config_f.nodesHeight))
    shape_f(shape=config_f.nodesShape , width = config_f.nodesWidth , height = config_f.nodesHeight)
    mainNodes_dict = shape_f.giveNodesDict()

    config_f.mainNodesDict = mainNodes_dict

    logger.info('Giving initial weight vector to the nodes')
    vectOperation_f = vectoroperation()
    vectOperation_f(sample_dict = mainSample_dict , nodes_dict = mainNodes_dict)
    vectOperation_f.giveInitialWeight()


    logger.info('Start training')
    training_f = training(config_f)
    if __name__ == '__main__':
        training_f.start()
    logger.debug('\n\n>>>> FINISH LOG <<<<\n')