from __future__ import division

__author__ = 'qunox'
import random , logging
from numpy import array , std, mean

class vectoroperation():

    def __init__(self):

        self.logger = logging.getLogger('sublog')

    def __call__(self, sample_dict = None, nodes_dict = None, *args, **kwargs):

        self.mainSample_dict = sample_dict
        self.mainNodes_dict =  nodes_dict
        self.sampleLength = len(self.mainSample_dict)
        self.nodesLength = len(self.mainNodes_dict)

        for item in [self.mainNodes_dict , self.mainNodes_dict]:
            if item is None:
                raise Exception('ERROR: %s could not be None'  % item)

        #checking sample vector dimension
        id = random.randint(0 , self.sampleLength)
        sampleVectorDimension = len(self.mainSample_dict[id]['vector'])

        _test_l = [[len(self.mainSample_dict[item]['vector']) , sampleVectorDimension] for item in self.mainSample_dict]

        def isitsame(item):
            if not item[0] == item[1]:
                return False

        _result_l = list(map(isitsame , _test_l))
        if False in _result_l:
            raise Exception('ERROR: Vector in sample dict does not have the same dimension')
        else:
            self.sampleVectorDimension = sampleVectorDimension
            self.logger.debug('Sample dict passes vector dimension check')

    def giveMeanaAndStd(self, sample_l):
        return mean(sample_l) , std(sample_l)

    def giveInitialWeight(self):

        _point_l = []

        for dimension in range(self.sampleVectorDimension):

            sampleVector_l = [self.mainSample_dict[id]['vector'][dimension] for id in range(self.sampleLength)]

            sampleMean , sampleStd = self.giveMeanaAndStd(sampleVector_l)

            initialVectorWeight_l = [random.gauss(sampleMean ,sampleStd) for i in range(self.nodesLength)]
            _point_l.append(initialVectorWeight_l)

        #combining the initial weight vector
        initialVectorWeight_l = []
        for i in range(self.nodesLength):
            _aVector = []
            for dimension in range(len(_point_l)):
                _aVector.append(_point_l[dimension][i])
            initialVectorWeight_l.append(array(_aVector))

        for node in self.mainNodes_dict:
            self.mainNodes_dict[node]['initialvector'] = initialVectorWeight_l[int(node)]
            self.mainNodes_dict[node]['vector'] = initialVectorWeight_l[int(node)]

