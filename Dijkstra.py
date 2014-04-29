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
  
  def algorithm(self,pathList,startVertex,goalVertex):
    curVertex = startVertex
    curVertex.distance = 0
    
    self.algorithmHelper(pathList,curVertex,goalVertex)

  def algorithmHelper(self,pathList,curVertex,goalVertex):
    #print "curVertex: %s" % curVertex.toString()
    for e in curVertex.nNL:
      #print "curVertex: ", curVertex.toString()
      destVertex = e.vertex1
      #print "destVertex: ", destVertex.toString()
      if (destVertex.visited == False):
        if ((e.length + curVertex.distance) < (destVertex.distance)):
          destVertex.distance = (e.length + curVertex.distance)
          #print "updated distance of : %s" % destVertex.toString()
          destVertex.previousVertex = curVertex
          #print "destVertex[",destVertex.toString(),"].previousVertex=[",curVertex.toString(),"]"
    # once all vertices in nNL are visited for current node, mark it as visited
    curVertex.visited = True
    #unvisitedVertices.remove(curVertex)
    #print "vertex removed: " ,curVertex.toString()
    
    # if destination node has been marked visited, we're done
    if(curVertex.equals(goalVertex)):
      print "done"
      return curVertex
  
    # now select unvisited node with smallest tentative distance
    smallestDistance = 1024 # infinity for our purposes
    smallestVertex = curVertex # just a placeholder

    for e in pathList:
      if (e.vertex0.visited == False):
        if (e.vertex0.distance < smallestDistance):
          smallestDistance = e.vertex0.distance
          smallestVertex = e.vertex0
    
    #print "about to call help on: ", smallestVertex.toString()
    if (smallestDistance < 1024):
      self.algorithmHelper(pathList,smallestVertex,goalVertex)
    else:
      return curVertex
      

