'''
@author: jsreese
'''

from Vertex import Vertex
from math import sqrt

class Edge:
  """ This object contains information about two linked vertices"""
  vertex0 = Vertex(0,0)
  vertex1 = Vertex(0,0)
  length = 0
  
  def __init__(self,firstVertex,secondVertex):
    self.vertex0 = firstVertex
    self.vertex1 = secondVertex
    self.length = sqrt((self.vertex1.x - self.vertex0.x)**2 + (self.vertex1.y - self.vertex0.y)**2)
    
  def toString(self):
    """Returns the string containing all an object's parameters"""
    return 'v0: (%s), v1: (%s), length: %s.' % \
      (self.vertex0.toString(), self.vertex1.toString(), self.length)