'''
@author: jsreese
'''

from PointRobot import PointRobot
import matplotlib.pyplot as plt
from CircleObstacle import CircleObstacle 
from Dijkstra import Dijkstra

def initializeObstacles():
  """ returns list of obstacles"""
  
  o0 = CircleObstacle(1,1,1)
  o1 = CircleObstacle(-1,-1,1)
  o2 = CircleObstacle(1,-1,1)
  o3 = CircleObstacle(-1,1,1)

  obstacleList = []
  obstacleList.extend([o0,o1,o2,o3])
  return obstacleList

def main():
  # assumes degree input in increments of 5
  #                  x,y,V,A,B,rV,D,dw
  robot = PointRobot(0,0,1,1,1,15,15,1)
  #print robot.toString()

  obstacleList = initializeObstacles()

  print "calculating coordinates"
  coordinatesTuple = robot.calcCoordinatesReachable(obstacleList)
  tupleList = coordinatesTuple[0] # list of reachable tuples
  behindObstacleList = coordinatesTuple[1] # list of tuples behind obstales
  print "tuple list: %s" %tupleList

  xList = []
  yList = []
  for t in tupleList:
    #print "x: %f, y: %f" % (t[0], t[1])
    xList.append(t[0])
    yList.append(t[1])
  #print "xList : %s" % xList
  #print "yList: %s" % yList
  
  oxList = []
  oyList = []
  for t in behindObstacleList:
    oxList.append(t[0])
    oyList.append(t[1])
    
  # find unreachable points via dijskstra's algorithm
  unreachableCoordinates = []
  d = Dijkstra(unreachableCoordinates)
  vertexList = d.genVertices(tupleList)
  print "calculating edges"
  edgeList = d.genPaths(vertexList,obstacleList)
  
  ex0List = []
  ey0List = []
  ex1List = []
  ey1List = []
  
  '''
  for e in edgeList:
    ex0List.append(e.vertex0.x)
    ey0List.append(e.vertex0.y)
    ex1List.append(e.vertex1.x)
    ey1List.append(e.vertex1.y)
    '''
    
  for e in edgeList:
    print "v0x (%s), v0y (%s), v1x (%s), v1y (%s)" % (e.vertex0.x, e.vertex0.y, e.vertex1.x, e.vertex1.y)
    #plt.plot((e.vertex0.x,e.vertex0.y),(e.vertex1.x, e.vertex1.y), color = 'k')
    x0 = e.vertex0.x
    y0 = e.vertex0.y
    x1 = e.vertex1.x
    y1 = e.vertex1.y
    plt.plot([x0,x1],[y0,y1],color = 'k')
  
  print "plotting coordinates"
  plt.plot(xList,yList,'ro')
  plt.plot(oxList,oyList,'bo')
  plt.ylabel('y')
  plt.xlabel('x')
  plt.title("reachable coordinates")
  #plt.axis([min(xList),max(xList) , min(yList), max(yList)])
  plt.axis([0,2 , 0, 2])

  
  
  plt.show()
  print "plotting complete"    
main()
