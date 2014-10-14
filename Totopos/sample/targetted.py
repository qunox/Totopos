from __future__ import division

import random
from numpy import array

class targetted():

    def giveSample(self):

        self.mainSample_l = []

        for i in range(1000):
            a = random.randint(0,5000)
            b = random.randint(0,5000)
            c = random.randint(0,5000)
            d = random.randint(0,5000)
            e = random.randint(0,5000)
            self.mainSample_l.append(['1' , array([0,0,a,b,c,0,0,0,d,e])])
            self.mainSample_l.append(['2' , array([0,0,-a,-b,-c,0,0,0,-d,-e])])
            self.mainSample_l.append(['3' , array([-a,-b,0,0,0,c,d,0,0,0])])
            self.mainSample_l.append(['4' , array([a,b,0,0,0,c,d,0,0,0])])
            self.mainSample_l.append(['5' , array([a,b,c,3,3,3,d,e,3,3])])
            self.mainSample_l.append(['6' , array([70,70,70,a,b,c,d,e,0,0])])
            self.mainSample_l.append(['7' , array([a,b,c,56,38,25,0,0,0,0])])
            self.mainSample_l.append(['8' , array([a,b,c,0,38,0,0,5,0,5])])
            self.mainSample_l.append(['9' , array([-a,b,-c,56,38,25,25,0,0,59])])
            self.mainSample_l.append(['10' , array([a,e,-b,-c,d,-d,-a,-e,b,c])])

        id = 0
        mainSample_d = {}

        for i in self.mainSample_l:

            mainSample_d[id]= {'vector' : i[1] , 'label' : i[0] }

            id += 1

        return mainSample_d


