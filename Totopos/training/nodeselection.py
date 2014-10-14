from __future__ import  division

from numpy import  array, linalg

class nodeselection():

    def __init__(self, mainNodesDict = None , mainSampleDict = None):

        self.mainNodesDict = mainNodesDict
        self.mainSampleDict = mainSampleDict

    def subtract_m(self, subtract_l):

        return [subtract_l[0],linalg.norm(subtract_l[1] - subtract_l[2])]


    def giveSmallest(self, sample_id):

        subtract_l = [[node, self.mainNodesDict[node]['vector'], self.mainSampleDict[sample_id]['vector']] for node in self.mainNodesDict]
        #doing the mapping
        subtracted_l = map(self.subtract_m , subtract_l)

        #picking the the minimum
        diff_l = [element[1] for element in subtracted_l]
        minDiff = min(diff_l)
        smallestIndex = diff_l.index(minDiff)

        return subtract_l[smallestIndex][0] , minDiff

    def giveNodeInRadius(self, selectedNode , radius):

        #puting all nodes position in list
        nodesPosition_l = [[node,self.mainNodesDict[selectedNode]['position'],self.mainNodesDict[node]['position'], radius] for node in self.mainNodesDict]

        def inRadius_m(nodePosition_l):

            length = linalg.norm(nodePosition_l[1] - nodePosition_l[2])

            if abs(length) <= nodePosition_l[3]:
                return [nodePosition_l[0], True]
            else:
                return [nodePosition_l[0], False]

        nodeInRadius_l = map(inRadius_m , nodesPosition_l)
        pickedNode_l = []

        for node in nodeInRadius_l:
            if node[1] is True:
                pickedNode_l.append(node[0])

        return pickedNode_l