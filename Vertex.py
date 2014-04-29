'''
@author: jsreese
'''
from __future__ import division

from math import sqrt, fabs


class Vertex:
  """This object contains information about a vertex's position"""
  x = 0
  y = 0
  nNL = [] #nearestNeighborList
  
  #for use with Dijsktra's algorithm
  distance = 1024 
  visited = False 
  previousVertex = None
  
  def __init__(self,theX,theY):
    self.x = theX
    self.y = theY
    
  def getDistance(self,otherVertex):
    """ returns distance between this node and another node"""
    return sqrt((otherVertex.x - self.x)**2 + (otherVertex.y - self.y)**2)
  
  def genNearestNeighbors(self,pathList,numNeighbors):
    """Initializes a vertex's list of numNeighbors nearest neighbors"""
    #actually numNeighbor edges with shortest lengths from self
    neighborList = []
    tempList = []
    for e in pathList:
      if (self.equals(e.vertex0)):
        tempList.append(e)

    tempList.sort(key=lambda x: x.length)

    if (len(tempList) < numNeighbors):
      trueNum = len(tempList)
    else:
      trueNum = numNeighbors
      
    for i in range(0,trueNum):
      neighborList.append(tempList[i])
    
    self.nNL = neighborList
    
  def toString(self):
    """Returns the string containing all an object's parameters"""
    return 'x: %s, y: %s, distance: %s.' % (self.x, self.y, self.distance)
    
  def equals(self,otherVertex):
    """Returns true if given vertex has same x and y as other vertex"""
    if(self.x == otherVertex.x and self.y == otherVertex.y):
      return True
    return False
      
  def clear(self, obstacleList):
    """Returns true if this robot is clear from all given obstacles"""
    for ob in obstacleList:
      if(((self.x - ob.x) ** 2) + ((self.y - ob.y) ** 2) < (ob.r ** 2)):
        return False
    return True
  
  def intersectsCircle(self,circle,destX,destY):
    """ Returns true if a vertex intersects a given circle"""
    
    tempX = self.x
    tempY = self.y
    if ((destX -self.x) == 0): # slope is undefined, so don't increment x
      i = 0
      while (i < abs(self.y - destY)):
        if (self.y < destY): # have to increment y to get to new point
          tempY += 0.1
        else: # self.Y is greater than destination, have to decrement it
          tempY -= 0.1
        if(((tempX - circle.x) ** 2) + ((tempY - circle.y) ** 2) < (circle.r ** 2)):
          return True
        i += 0.1
      return False   
    else: # slope is okay
      slope = ((destY - self.y)/(destX - self.x))
      i = 0
      while (i < abs(self.x - destX)):
        if(self.x < destX): # have to increment x to get to new point
          #increment x by 1 every iteration, and y by the slope
          tempX += 0.1
          tempY += slope * 0.1
        else: # x is greater than destination, have to decrement it
          tempX -= 0.1
          tempY -= slope * 0.1
        if(((tempX - circle.x) ** 2) + ((tempY - circle.y) ** 2) < (circle.r ** 2)):
          return True
        i += 0.1
      return False
      
  
  ''' this is incorrect, treats points between two as lines not rays
  def intersectsCircle(self, circle, destX, destY):
    """ Returns true if line between self and (destX,destY) intersects circle"""
    # distance between robot and destination point 
    dist = sqrt((destX - self.x)**2 + (destY - self.y)**2)
    
    # compute direction vector D from robot to destination
    Dx = (destX -self.x)/dist
    Dy = (destY - self.y)/dist
    
    # closest point to the circle center
    t = Dx*(circle.x -self.x) + Dy*(circle.y-self.y)
    
    # coordinates of point E on line that is closest to C
    Ex = t*Dx+self.x
    Ey = t*Dy+self.y
    
    #compute distance from E to C
    distEC = sqrt((Ex-circle.x)**2 + (Ey-circle.y)**2)
    
    print "distEC: ", distEC, "circle: ", circle.x, circle.y, circle.r
    print "Ex: ", Ex, " Ey: ", Ey

    if (distEC < circle.r):
      return True
    return False
    '''
  
  def link(self, obstacleList, otherVertex):
    """Returns true if the straight-line path between (x,y) and (destX,destY) is collision free"""
    for ob in obstacleList:
      #print "self:", self.x, self.y, "other:", otherVertex.x, otherVertex.y
      if(self.intersectsCircle(ob,otherVertex.x,otherVertex.y)):
        return False
      
    return True
  
  
  
  
  
  
  