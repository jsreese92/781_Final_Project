'''
@author: jsreese
'''

from PointRobot import PointRobot
import matplotlib.pyplot as plt

def main():
  # assumes degree input in increments of 5
  #                  x,y,V,A,B,rV,D,dw
  robot = PointRobot(0,0,1,1,1,15,0,1)
  #print robot.toString()

  print "calculating coordinates"
  tupleList = robot.calcCoordinatesReachable()
  print "tuple list: %s" %tupleList

  xList = []
  yList = []
  for t in tupleList:
    #print "x: %f, y: %f" % (t[0], t[1])
    xList.append(t[0])
    yList.append(t[1])
  #print "xList : %s" % xList
  #print "yList: %s" % yList
  
  print "plotting coordinates"
  plt.plot(xList,yList,'ro')
  plt.ylabel('y')
  plt.xlabel('x')
  plt.axis([-1.5, 1.5, -1.5, 1.5])

  plt.show()
  print "plotting complete"
    
main()