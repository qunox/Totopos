from __future__ import  division
import logging
from numpy import array

class shape():

    def __init__(self):
        self.logger = logging.getLogger('sublog')

    def __call__(self, *args, **kwargs):

        if 'shape' in kwargs:
            self.shape = kwargs['shape']
        if 'width' in kwargs:
            self.width = int(kwargs['width'])
        if 'height' in kwargs:
            self.height = int(kwargs['height'])

        if not hasattr(self, 'shape'):
            raise Exception('ERROR: No shape was given to node')

        if self.shape is 'rectangular':
            self.rectangular()

    def rectangular(self):

        self.logger.debug('Creating a rectangular shape nodes')
        nodePosition = [array([x,y]) for x in range(self.width) for y in range(self.height)]

        self.nodes_dict = {}
        _i = 0

        for position in nodePosition:
            self.nodes_dict[_i] = {'position' : position , 'initialvector' : None, 'label': '0' , 'vector':None , 'popularity' : 0,
                                    'picked' : 0 , 'perturb' : 0 }
            _i += 1

        self.logger.debug('Finish rectangular creating nodes')

    def giveNodesDict(self):

        if hasattr(self , 'nodes_dict'):
            return self.nodes_dict
        else:
            raise  Exception('Nodes dict has not been created yet')