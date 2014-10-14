__author__ = 'qunox'

from multiprocessing import Pool
import random

def addRandomly(element_l):

    return element_l[0] + element_l[1]*random.random()

def mapFunction(listed_l):

    newList = map(addRandomly , listed_l)
    return min(newList)

if __name__ == '__main__':

    listed_l = []
    for i in range(1000):
        listed_l.append([random.random(), random.random()])

    pool_f = Pool()
    newly_l = pool_f.map(mapFunction, listed_l)