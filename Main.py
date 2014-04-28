'''
@author: jsreese
'''

from PointRobot import PointRobot
import matplotlib.pyplot as plt
from CircleObstacle import CircleObstacle 

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
  robot = PointRobot(0,0,1,1,1,120,90,3)
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
    
  print "plotting coordinates"
  plt.plot(xList,yList,'ro')
  plt.plot(oxList,oyList,'bo')
  plt.ylabel('y')
  plt.xlabel('x')
  plt.title("reachable coordinates")
  plt.axis([min(xList),max(xList) , min(yList), max(yList)])
  plt.show()
  print "plotting complete"
  

  
    
  print "plotting behind obstacles"
  plt.plot()
    
main()
