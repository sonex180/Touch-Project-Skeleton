import xml.etree.ElementTree as ET
import sys

tags = []
def findCircle(element):
  global tags
  for child in element:
    if child.tag in ['{http://www.w3.org/2000/svg}circle', 'circle']:
      tags.append(child)
    else:
      findCircle(child)

doc = ET.parse("drawing.svg")
svg = doc.findall(".")[0]
width = svg.attrib['width'].replace('px','')
height = svg.attrib['height'].replace('px','')
canvasSize = [ int(width), int(height) ]
print("Document: {} x {}".format(*canvasSize))

root = doc.getroot()
findCircle(root)

if len(tags) == 0:
  print('No circles found')
  sys.exit(0)

fileBufferX = open('outputPositionsX.txt', 'w')
fileBufferY = open('outputPositionsY.txt', 'w') 

for ball in tags:
  radius = float(ball.attrib['r'])
  ballSize = [ float(ball.attrib['cx']), 
    canvasSize[1] - float(ball.attrib['cy']) ]

  for i in range(0, len(ballSize)):
    ballSize[i] /= canvasSize[i]

    # Convert range from [0,1] to [-1, 1]
    ballSize[i] = ballSize[i] * 2 - 1

  fileBufferX.write("{}\n".format(ballSize[0]))
  fileBufferY.write("{}\n".format(ballSize[1]))

