'''
@author: jsreese
'''

from PointRobot import PointRobot
from Vertex import Vertex
import matplotlib.pyplot as plt
from CircleObstacle import CircleObstacle 
from Dijkstra import Dijkstra
import time

def initializeObstacles():
  """ returns list of obstacles"""
  
  o0 = CircleObstacle(0,1,.5)
  o1 = CircleObstacle(-1,-1,.5)
  o2 = CircleObstacle(1,-1,.5)
  o3 = CircleObstacle(-1,1,.5)

  obstacleList = []
  obstacleList.extend([o0,o1,o2,o3])
  return obstacleList

def main():
  # assumes degree input in increments of 5
  #                  x,y,V,A,B,rV,D,dw
  
  '''
  velocities = [2]
  rotationalVelocities = [15,30,45,90,180]
  dynamicWindows = [0.5,1,1.5,2]
  for velocity in velocities:
    for rotational in rotationalVelocities:
      for dynamic in dynamicWindows:
        print" v: %s, r: %s, dw: %s" % (velocity, rotational, dynamic)
        startTime = time.time()
        robot = PointRobot(0,0,velocity,1,1,rotational,90,dynamic)
        #print robot.toString()

        obstacleList = initializeObstacles()

        #print "calculating coordinates"
        coordinatesTuple = robot.calcCoordinatesReachable(obstacleList)
        tupleList = coordinatesTuple[0] # list of reachable tuples
        behindObstacleList = coordinatesTuple[1] # list of tuples behind obstales
        #print "tuple list: %s" %tupleList

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
        
        #print "initializing vertices behind obstacles"
        verticesBehindObstacles = []
        for v in vertexList:
          for t in behindObstacleList:
            if ((v.x == t[0]) and (v.y == t[1])):
                verticesBehindObstacles.append(v)
        #print "vertices behind obstacles initialized"
                
        #print "calculating edges"
        pathList = d.genPaths(vertexList,obstacleList)
        #print "edges calculated"
        
        # select m nearest neighbors for each vertex
        #print "generating nearest neighbors"
        startVertex = Vertex(0,0)
        vertexList.append(startVertex)
        for v in vertexList:
          v.genNearestNeighbors(pathList,3)
        for v in verticesBehindObstacles:
          v.genNearestNeighbors(pathList,3)
          #for n in v.nNL:
          #  print "nearest neighbor list: %s" % n.toString()
        #startVertex.genNearestNeighbors(pathList, 3)
        #print "nearest neighbors generated"
          
        vi = robot.tV # initial velocity
        a = robot.tA
        t = robot.dw # length of time is just length of dynamic window
        vf = vi + a * t # final velocity

        # max distance that can be traveled 
        maxDistance = ((vi + vf)/2)*t
       
        #print "running dijkstras on vertices behind obstacles"
        for v in verticesBehindObstacles:
          #print "v: %s" % v.toString()
          #for n in v.nNL:
          #  print "nearest neighbor list: %s" % n.toString()
          d.algorithm(pathList,startVertex,v)
          if (v.distance > maxDistance):
            #print "v: %s" % v.toString()

            d.unreachableCoordinates.append(v)
            #print "unreachable: %s " % v.toString()
            #for n in v.nNL:
            #  print "unreachable's nearest neighbor list: %s" % n.toString()
        #print "dijkstras complete"
        
        # unreachable vertices
        uxList = []
        uyList = []
        for v in unreachableCoordinates:
          uxList.append(v.x)
          uyList.append(v.y)
          
        
        # plots edges (takes a while)
        #for e in pathList:
          #print "v0x (%s), v0y (%s), v1x (%s), v1y (%s)" % (e.vertex0.x, e.vertex0.y, e.vertex1.x, e.vertex1.y)
          #x0 = e.vertex0.x
          #y0 = e.vertex0.y
          #x1 = e.vertex1.x
          #y1 = e.vertex1.y
          #plt.plot([x0,x1],[y0,y1],color = 'k')
          
        '''
  '''
        print "plotting coordinates"
        direct = plt.plot(xList,yList,'go')
        around = plt.plot(oxList,oyList,'yo')
        unreachable = plt.plot(uxList,uyList,'ro')


        plt.ylabel('y')
        plt.xlabel('x')
        plt.title("reachable coordinates")
        plt.axis([min(xList),max(xList) , min(yList), max(yList)])
        
        #plt.legend([direct,around,unreachable], ["straight path", "around obstacle", "unreachable"])
        #plt.axis([0,2 , 0, 2])

        
        
        plt.show()
        print "plotting complete"     
        '''
  '''
        totalTime = time.time() - startTime
        print "total time: %f" % totalTime
        '''

  
  
  robot = PointRobot(0,0,1,1,1,45,90,1)
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
  
  '''
  print "initializing vertices behind obstacles"
  verticesBehindObstacles = []
  for v in vertexList:
    for t in behindObstacleList:
      if ((v.x == t[0]) and (v.y == t[1])):
          verticesBehindObstacles.append(v)
  print "vertices behind obstacles initialized"
  
    '''      
  print "calculating edges"
  pathList = d.genPaths(vertexList,obstacleList)
  print "edges calculated"
  
  '''
  # select m nearest neighbors for each vertex
  print "generating nearest neighbors"
  startVertex = Vertex(0,0)
  vertexList.append(startVertex)
  for v in vertexList:
    v.genNearestNeighbors(pathList,3)
  for v in verticesBehindObstacles:
    v.genNearestNeighbors(pathList,3)
    #for n in v.nNL:
    #  print "nearest neighbor list: %s" % n.toString()
  #startVertex.genNearestNeighbors(pathList, 3)
  print "nearest neighbors generated"
    
  vi = robot.tV # initial velocity
  a = robot.tA
  t = robot.dw # length of time is just length of dynamic window
  vf = vi + a * t # final velocity

  # max distance that can be traveled 
  maxDistance = ((vi + vf)/2)*t
 
  
  print "running dijkstras on vertices behind obstacles"
  for v in verticesBehindObstacles:
    #print "v: %s" % v.toString()
    #for n in v.nNL:
    #  print "nearest neighbor list: %s" % n.toString()
    d.algorithm(pathList,startVertex,v)
    if (v.distance > maxDistance):
      print "v: %s" % v.toString()

      d.unreachableCoordinates.append(v)
      #print "unreachable: %s " % v.toString()
      #for n in v.nNL:
      #  print "unreachable's nearest neighbor list: %s" % n.toString()
  print "dijkstras complete"
  '''
  '''
  # unreachable vertices
  uxList = []
  uyList = []
  for v in unreachableCoordinates:
    uxList.append(v.x)
    uyList.append(v.y)
    
  '''
  # plots edges (takes a while)
  
  for e in pathList:
    #print "v0x (%s), v0y (%s), v1x (%s), v1y (%s)" % (e.vertex0.x, e.vertex0.y, e.vertex1.x, e.vertex1.y)
    x0 = e.vertex0.x
    y0 = e.vertex0.y
    x1 = e.vertex1.x
    y1 = e.vertex1.y
    plt.plot([x0,x1],[y0,y1],color = 'k')
    
  
  print "plotting coordinates"
  direct = plt.plot(xList,yList,'go')
  #around = plt.plot(oxList,oyList,'yo')
  #unreachable = plt.plot(uxList,uyList,'ro')


  plt.ylabel('y')
  plt.xlabel('x')
  plt.title("reachable coordinates")
  plt.axis([min(xList),max(xList) , min(yList), max(yList)])
  
  #plt.legend([direct,around,unreachable], ["straight path", "around obstacle", "unreachable"])
  #plt.axis([0,2 , 0, 2])

  
  plt.show()
  print "plotting complete"  
  
  
main()
