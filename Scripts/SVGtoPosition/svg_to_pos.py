import xml.etree.ElementTree as ET
import sys

tags = []
def findCircle(element):
  global tags
  for child in element:
    tagFormatted = child.tag.replace('{http://www.w3.org/2000/svg}', '')
    if tagFormatted in ['circle', 'ellipse']:
      tags.append(child)
    else:
      findCircle(child)

doc = ET.parse("drawing.svg")
svg = doc.findall(".")[0]

if 'width' in svg.attrib and 'height' in svg.attrib:
  width = svg.attrib['width'].replace('px','')
  height = svg.attrib['height'].replace('px','')
elif 'viewBox' in svg.attrib:
  viewbox = svg.attrib['viewBox'].split(' ')
  width = viewbox[2]
  height = viewbox[3]

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
  ballSize = [ float(ball.attrib['cx']), 
    canvasSize[1] - float(ball.attrib['cy']) ]

  for i in range(0, len(ballSize)):
    ballSize[i] /= canvasSize[i]

    # Convert range from [0,1] to [-1, 1]
    ballSize[i] = ballSize[i] * 2 - 1

  fileBufferX.write("{}\n".format(ballSize[0]))
  fileBufferY.write("{}\n".format(ballSize[1]))

