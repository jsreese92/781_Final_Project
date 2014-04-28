'''
@author: jsreese
'''

class CircleObstacle:
  """ This object contains information about 2D circle obstacles"""
  x = 0
  y = 0
  r = 0
  
  def __init__(self,theX,theY,theRadius):
    self.x = theX
    self.y = theY
    self.r = theRadius
    
  def toString(self):
    """Returns the string containing all an object's parameters"""
    return 'x coordinate: %s, y coordinate: %s, radius: %s.' % \
      (self.x, self.y, self.r)
