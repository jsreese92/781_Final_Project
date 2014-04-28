'''
@author: jsreese
'''

from math import pow, radians, degrees, cos, sin

class PointRobot: 
  """ This object contains information about our point robot"""
  x = 0
  y = 0
  tV = 0 # translational Velocity (m/s)
  tA = 0 # translational acceleration (m/s2)
  bA = 0 # braking acceleration (m/s2)
  rV = 0 # max rotational velocity (degrees/s)
  cD = 0 # current degree/angle (degrees)
  dw = 1 # length of dynamic window (s)

  def __init__(self, theX, theY, theTV, theTA, theBA, theRV, theCD, theDw):
    self.x = theX
    self.y = theY
    self.tV = theTV
    self.tA = theTA
    self.bA = theBA
    self.rV = theRV
    self.cD = theCD
    self.dw = theDw
    

  def toString(self):
    """Returns string containing all this object's paramerters"""
    return 'x: %s, y: %s, tV: %s, tA: %s, bA: %s, rv: %s, dw: %s.' % \
        (self.x, self.y, self.tV, self.tA, self.bA, self.rV, self.dw)
        
  def clearCircleObstacles(self,obstacleList,x,y):
    """ returns whether points x and y intersect any circle obstacles"""
    for ob in obstacleList:
      if(((x - ob.x) ** 2) + ((y - ob.y) ** 2) < (ob.r ** 2)):
        return False
    return True
          
  def calcCoordinatesReachable(self, obstacleList):
    """ Returns list of (x,y) tuples at 0.1 m intervals reachable"""
    vi = self.tV # initial velocity
    a = self.tA
    t = self.dw # length of time is just length of dynamic window
    vf = vi + a * t # final velocity

    # max distance that can be traveled 
    d = ((vi + vf)/2)*t

    currentAngle = self.cD
    maxAngle = (currentAngle + (self.rV*t))%360
    minAngle = (currentAngle - (self.rV*t))%360

    # places points in list that can be reached within dynamic window
    # line-first method of doing it
    tempAngle = maxAngle # (degrees)
    #minAngle = minAngle #(degrees)
    tempList = []
    iteratorNum = -5 # decrements from max to min angle by 5 degrees
    
    
    # emulate do-while loop in python
    condition = True
    while condition:
      i = 0 #(m)
      #print "out: tempAngle: %s, minAngle %s" %(tempAngle, minAngle)
      while (i < d):
        newX = round(i*cos(radians(tempAngle)),2)
        newY = round(i*sin(radians(tempAngle)),2)   
        tempTuple = (newX,newY)
        tempList.append(tempTuple)
        i += 0.1
      tempAngle += iteratorNum
      
      # update do-while
      condition = (tempAngle != minAngle)

      if (tempAngle > 360):
        tempAngle = tempAngle - 360
      elif (tempAngle < 0):
        tempAngle = tempAngle + 360
    
      # line where tempAngle == minAngle
      i = 0
      while (i < d):
        newX = round(i*cos(radians(minAngle)),2)
        newY = round(i*sin(radians(minAngle)),2)
        tempTuple = (newX,newY)
        tempList.append(tempTuple)
        i += 0.1


#    # angle-first way of doing it
#    i = 0 # (m)
#    tempList = []
#    while (i < d):
#      #print "i: %s" %i
#      tempAngle = maxAngle # (degrees)
#      minAngle = minAngle # (degrees)
#      #print "out: tempAngle: %s, minAngle %s" %(tempAngle, minAngle)
#      iteratorNum = 0 # number by which to increment angle
#      if (tempAngle < minAngle):
#        #print "angles flipped"
#        #tempAngle = 360 - tempAngle
#        #minAngle = 360 - minAngle
#        iteratorNum = -5
#      else:
#        iteratorNum = 5
#        
#      while (tempAngle != minAngle): 
#        #print "mid tempangle: %s, minAngle: %s" % (tempAngle, minAngle)
#        #print "cos: %s, sin: %s" % (cos(radians(tempAngle)), sin(radians(tempAngle)))
#        newX = round(i*cos(radians(tempAngle)),2)
#        newY = round(i*sin(radians(tempAngle)),2)
#        #print "newX: %s, newY: %s" % (newX,newY)
#        tempAngle += iteratorNum # decrement 5 degrees, arbitrary
#        if (tempAngle > 360):
#          tempAngle = tempAngle - 360
#        if (tempAngle < 0):
#          tempAngle = tempAngle + 360
#          
#        tempTuple = (newX,newY)
#        tempList.append(tempTuple)
#
#      i += 0.1 # increment one tenth of a meter each time
    
    # remove duplicates
    tupleList = sorted(tempList)
    for t in tempList:
      #print "removing duplicates"
      if tupleList.count(t) > 1:
        tupleList.remove(t)
      
    return tupleList


