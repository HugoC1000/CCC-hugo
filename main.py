def J5():
  import matplotlib.pyplot as plt

  def growUp(startPos, endPos):
    width = abs(endPos[0] - startPos[0])
    width /= 3
    width = int(width)
    turn1 = [startPos[0] + width, startPos[1]]
    turn2 = [startPos[0] + width, startPos[1] + width]
    turn3 = [startPos[0] + width * 2, startPos[1] + width]
    turn4 = [startPos[0] + width * 2, startPos[1]]
    return [startPos,
            turn1], [turn1, turn2], [turn2, turn3], [turn3,
                                                     turn4], [turn4, endPos]

  def growDown(startPos, endPos):
    width = abs(endPos[0] - startPos[0])
    width /= 3
    width = int(width)
    turn1 = [startPos[0] - width, startPos[1]]
    turn2 = [startPos[0] - width, startPos[1] - width]
    turn3 = [startPos[0] - width * 2, startPos[1] - width]
    turn4 = [startPos[0] - width * 2, startPos[1]]
    return [startPos,
            turn1], [turn1, turn2], [turn2, turn3], [turn3,
                                                     turn4], [turn4, endPos]

  def growLeft(startPos, endPos):
    width = abs(endPos[1] - startPos[1])
    width /= 3
    width = int(width)
    turn1 = [startPos[0], startPos[1] + width]
    turn2 = [startPos[0] - width, startPos[1] + width]
    turn3 = [startPos[0] - width, startPos[1] + width * 2]
    turn4 = [startPos[0], startPos[1] + width * 2]
    # print(turn1, turn2, turn3, turn4)
    return [startPos,
            turn1], [turn1, turn2], [turn2, turn3], [turn3,
                                                     turn4], [turn4, endPos]

  def growRight(startPos, endPos):
    width = abs(endPos[1] - startPos[1])
    width /= 3
    width = int(width)
    turn1 = [startPos[0], startPos[1] - width]
    turn2 = [startPos[0] + width, startPos[1] - width]
    turn3 = [startPos[0] + width, startPos[1] - width * 2]
    turn4 = [startPos[0], startPos[1] - width * 2]
    return [startPos,
            turn1], [turn1, turn2], [turn2, turn3], [turn3,
                                                     turn4], [turn4, endPos]

  def routing(startPos, endPos):
    if startPos[1] == endPos[1] and startPos[0] < endPos[0]:
      # print("growUp")
      return growUp(startPos, endPos)
    elif startPos[1] == endPos[1] and startPos[0] > endPos[0]:
      # print("growDown")
      return growDown(startPos, endPos)
    elif startPos[1] < endPos[1] and startPos[0] == endPos[0]:
      # print("growLeft")
      return growLeft(startPos, endPos)
    elif startPos[1] > endPos[1] and startPos[0] == endPos[0]:
      # print("growRight")
      return growRight(startPos, endPos)
    else:
      print("invalid points")
      return []

  def makeRoute(startPos, endPos, level):
    route = [[startPos, endPos]]
    for i in range(level):
      runs = len(route)
      for j in range(runs):
        lu = routing(route[0][0], route[0][1])
        route += lu
        # print("lu ",lu)
        route.pop(0)
    return route

  def makePointList(edges):
    pointList = []
    for edge in edges:
      for point in edge:
        point = tuple(point)
        if point not in pointList:
          pointList.append(point)
    return pointList

  def drawFractal(start, end, level, xInter):
    getX = lambda tup: tup[0]
    getY = lambda tup: tup[1]
    plotEdges = makeRoute([start[0], start[1]], [end[0], end[1]], level)
    # print(plotEdges)
    plotPoints = makePointList(plotEdges)
    yInter = []
    for point in plotPoints:
      if xInter == point[0]:
        yInter.append(point[1])
    for edge in plotEdges:
      # print(edge)
      if xInter > edge[0][0] and xInter < edge[1][0]:
        if edge[0][1] not in yInter:
          yInter.append(edge[0][1])
      if xInter < edge[0][0] and xInter > edge[1][0]:
        if edge[0][1] not in yInter:
          yInter.append(edge[0][1])
    yInter.reverse()
    print(*yInter)
    pointsX = list(map(getX, plotPoints))
    pointsY = list(map(getY, plotPoints))
    plt.plot(pointsX, pointsY)
    plt.show()

  line = input()
  line = list(map(int, line.split()))
  level = line[0]
  width = line[1]
  xIntersect = line[2]
  drawFractal([0,1],[width, 1], level, xIntersect)

J5()


# https://dmoj.ca/problems/

# def h1(k):
#   return (2*k+5)%11
# def h2(k):
#   return 7-(k%7)

# def probe(i):
#   pass

# List = [12,44,13,88,23,94,11]
# Array = [0]*11
# for a in List:
#   f1 = h1(a)
#   for i in range(11):
#     if Array[f1] == 0:
#       Array[f1] = a
#       break
#     else:
#       f2 = h1(a)+h2(a)
#       if Array[f2%11] == 0:
#         Array[f2%11] = a
#         break
# print(Array)
        

# input1 = int(input())
# input2 = int(input())
# inp = [input1,input2]
# count = 0
# secount = 0
# for a in range(inp[0],inp[1]+1,1):
#     for b in range(1,a+1,1):
#         if a%b == 0:
#             count += 1
#         if count > 4:
#             break
#     if count == 4:
#         secount += 1
#     count = 0
    
# print(secount)

