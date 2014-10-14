__author__ = 'qunox'
import time
import random

print 'Creating list A'

listA = [random.random() for i in range(100000)]

startTime = time.time()

listB = [random.choice(listA) for i in range(100000)]

endTime = time.time()

print "required time:" , startTime-endTime