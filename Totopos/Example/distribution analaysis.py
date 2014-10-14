__author__ = 'qunox'
import random
from numpy import std , mean

sample = [random.gauss(2,0.5) for i in range(1000)]

sample_std = std(sample)
sample_mean = mean(sample)


print 'std:' , sample_std
print 'mean:' , sample_mean
