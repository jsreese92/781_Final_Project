'''
Created on Apr 28, 2014

@author: jsreese
'''

import random
from Vertex import Vertex 
from Edge import Edge

class Dijkstra:
  unreachableCoordinates = []
  
  def __init__(self,theCoordinates):
    self.unreachableCoordinates = theCoordinates
  
  def genVertices(self, tupleList):
    """ returns list of vertices of type Vertex from reachable tuples"""
    vertexList = []
    for t in tupleList:
      v = Vertex(t[0],t[1])
      vertexList.append(v)
    
    #for v in vertexList:
    #  print"x: %s, y: %s" % (v.x, v.y)
    #  print "vertex list printed"
    return vertexList

  def genPaths(self,vertexList,obstacleList):
    edgeList = []
    for v0 in vertexList:
      for v1 in vertexList:
        if(not v0.equals(v1)): # don't care about edges from a vertex to itself
          if (v0.link(obstacleList,v1)): # if clear path exists from v0 to v1
            e = Edge(v0,v1)
            # print "edge from %s, %s to %s, %s connected" % (v0.x, v0.y, v1.x, v1.y)
            edgeList.append(e)
    #for e in edgeList:
    #  print "v0: %s, v1: %s" % (e.vertex0.toString(), e.vertex1.toString())
    #print "edges printed"
    return edgeList

