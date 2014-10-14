from __future__ import  division
__author__ = 'qunox'

import logging
from numpy import exp

class decayfunction():

    def __init__(self):
        self.logger = logging.getLogger('sublog')

    def expondecay(self, maxValue , decayRate , value):
        if decayRate > 0: self.logger.debug('WARNING: decay rate > 0')
        expValue = decayRate* value
        return maxValue*exp(expValue)

