__author__ = 'qunox'

from numpy import array
from numpy import  linalg
#created a grid of node

nodeshieght = 20
nodeswidth = 60

nodesdict = {}

id = 0
for y in range(nodeshieght):
    for x in range(nodeswidth):
        nodesdict[id]={'position' : array([x,y]) , 'vector' : 0}
        id += 1


radius = 0.9*nodeshieght
pickedposition = array([30,10])

for node in nodesdict:
    if linalg.norm(nodesdict[node]['position'] - pickedposition) < radius:
        nodesdict[node]['vector'] = 'x'


for y in range(nodeshieght):
    line = ''
    for x in range(nodeswidth):
        for node in nodesdict:
            if nodesdict[node]['position'][0] == x and nodesdict[node]['position'][1] == y:
                line += str(nodesdict[node]['vector'])+' '

    print line