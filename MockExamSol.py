def J1():
  inpa = int(input(""))
  inpb = int(input(""))
  inpc = int(input(""))

  l = [inpa, inpb, inpc]
  l.sort()
  print(l[1])


# J1()


def J2():
  valid = False
  while valid is False:
    lower = int(input())
    upper = int(input())
    if lower <= upper:
      valid = True
    else:
      print("The lower limit is higher than upper limit")
  counter = 0
  for RSA in range(lower, upper + 1):
    divisor = 0
    for i in range(1, RSA + 1):
      if RSA % i == 0:
        divisor += 1
    if divisor == 4:
      counter += 1
    divisor = 0
  print(f'The number of RSA numbers between {lower} and {upper} is {counter}')


# J2()


def J3():
  quarter = int(input())
  first = int(input())
  second = int(input())
  third = int(input())
  slotMachine = [first, second, third]
  machineTrigger = (35, 100, 10)
  machinePay = {35: 30, 100: 60, 10: 9}
  totalCount = 0
  while quarter > 0:
    quarter -= 1
    slotMachine[totalCount % 3] += 1
    if (slotMachine[totalCount % 3] == machineTrigger[totalCount % 3]):
      slotMachine[totalCount % 3] = 0
      quarter += machinePay[machineTrigger[totalCount % 3]]
    totalCount += 1

  print(f'Martha plays {totalCount} times before going broke.')


# J3()

import math


def J4():
  numerator = int(input())
  denominator = int(input())
  zhengshu = (int)(numerator / denominator)
  fenzi = (int)(numerator % denominator)
  gcd = math.gcd(fenzi, denominator)
  fenzi = (int)(fenzi / gcd)
  fenmu = (int)(denominator / gcd)
  output = ""
  if fenzi == 0 and zhengshu == 0:
    output += str(0)
  else:
    if zhengshu > 0:
      output += str(zhengshu)
    if zhengshu > 0 and fenzi > 0:
      output += " "
    if fenzi > 0:
      output += str(fenzi) + "/" + str(fenmu)
  print(output)


# J4()


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
  drawFractal([0, 1], [width, 1], level, xIntersect)


J5()
