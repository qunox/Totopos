from __future__ import division

import os
import datetime

from os import path
from numpy import linalg

class draw():

    def __init__(self, mainNodesDict, mainSampleDict , config):

        self.mainNodesDict = mainNodesDict
        self.mainSampleDict = mainSampleDict
        self.config = config

    def textDrawMainNodes(self):

        vectorCanvas = []
        labelCanvas = []
        for y in range(self.config.nodesHeight):
            y_l = []
            for x in range(self.config.nodesWidth):
                y_l.append(None)
            vectorCanvas.append(y_l)

        for y in range(self.config.nodesHeight):
            y_l = []
            for x in range(self.config.nodesWidth):
                y_l.append(None)
            labelCanvas.append(y_l)

        for node in self.mainNodesDict:
            x = self.mainNodesDict[node]['position'][0]
            y = self.mainNodesDict[node]['position'][1]

            vectorCanvas[y][x] = self.mainNodesDict[node]['vector']
            labelCanvas[y][x] = self.mainNodesDict[node]['label']

        #creating a new draw directory if it didnt exist

        drawingDirectory = path.join(self.config.projectDirectory , 'drawing')
        if not path.exists(drawingDirectory): os.mkdir(drawingDirectory)

        canvasFileName = path.join(drawingDirectory , datetime.datetime.now().strftime('%Y_%m_%d_%H%M%S_canvas.txt'))
        canvas_f = open(canvasFileName , 'w')

        canvas_f.write('\n\n\nVector\n')

        for y in vectorCanvas:
            line = ''
            for x in y:
                line += str(x) + ','
            line = line + '\n'
            canvas_f.write(line)

        canvas_f.write('\n\nMagnitude\n')

        for y in range(len(vectorCanvas)):
            line = ''
            for x in range(len(vectorCanvas[y])):
                line += str(linalg.norm(vectorCanvas[y][x])) + ','
            line = line + '\n'
            canvas_f.write(line)

        canvas_f.write('\n\nLabel\n')
        for y in range(len(labelCanvas)):
            line = ''
            for x in range(len(labelCanvas[y])):
                line += str(labelCanvas[y][x]) + ','
            line = line + '\n'
            canvas_f.write(line)

        canvas_f.close()


