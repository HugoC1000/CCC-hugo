#15/15 Good
def J1():
  inpa = int(input(""))
  inpb = int(input(""))
  inpc = int(input(""))

  l = [inpa, inpb, inpc]
  l.sort()
  print(l[1])


J1()


# wrong question answered
def J2():
  pass


J2()


#should be 15/15, make sure your output is consistent with the question
#CCC rule: Output must match the output format specified in the problem exactly. Prompts or additional output must not be produced.
def J3():
  #changed below
  quater = int(input())
  f = int(input())
  s = int(input())
  t = int(input())
  count = [f, s, t]
  d = {35: 30, 100: 60, 10: 9}
  req = [35, 100, 10]
  subcount = 0
  actualcounter = 0

  while quater > 0:
    quater -= 1  #Subtract a quater when play
    # print(count)
    count[subcount] += 1  #Add 1 to the machine that is being played
    if count[subcount] == req[subcount]:
      quater += d[req[subcount]]
      count[subcount] = 0
    subcount += 1  #Rotate through the machines
    if subcount > 2:
      subcount = 0
    actualcounter += 1

  # print(actualcounter)
  #change below
  print("Martha plays " + str(actualcounter) + " times before going broke.")


# J3()

#3.33/15
def J4():

  def greatfactor(numerator, denominater):
    while denominater != 0:
      numerator, denominater = denominater, numerator % denominater
    gcf = numerator
    return gcf

  def fractionwriter(finalnum, finalden):
    if finalnum == 0:
      print("0")
    elif finalden == 1:
      print(finalnum)
    elif finalnum == finalden:
      print("1")
    elif finalnum > finalden:
      integerpart, finalnum = improperfraction(finalnum, finalden)
      print(integerpart, " ", finalnum, "/", finalden, sep="")

  def improperfraction(finalnum, finalden):
    integerpart = finalnum // finalden
    newnum = finalnum - integerpart * finalden
    return integerpart, newnum

  numerator = int(input())
  denominater = int(input())

  gcf = greatfactor(numerator, denominater)
  newnum = int(numerator / gcf)
  newden = int(denominater / gcf)
  fractionwriter(newnum, newden)


# J4()

#0/15
def J5():
  pass
