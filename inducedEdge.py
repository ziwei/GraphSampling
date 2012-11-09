import depend

sumDW = 0.0
sum1W = 0.0
sum1WW = 0.0
sum1EWW = 0.0
sum1JW = 0.0
prevIDegree = 0.0
inducedEdgeNum = 0

def inducedEdge(sampleList, friendList, breakDep, theta) :
   print "+++Induced Edge+++"
   noDependList = []
   noDependFriendList = []
   if breakDep == 0 :
       noDependList = depend.thinningsample(sampleList, theta,0)
       noDependFriendList = depend.thinningfriend(friendList, theta,0)
       print "***Simple Thinning***"
       print "Estimated Size of nodes :" + str(getListResult(noDependList, noDependFriendList))
       print "Induced Edges :" + str(inducedEdgeNum)
   elif breakDep == 1 :
       totalNodeSize = 0
       for i in range(0,theta-1) :
           noDependList = depend.thinningsample(sampleList,theta,i)
	   noDependFriendList = depend.thinningfriend(friendList, theta,0)
           totalNodeSize = totalNodeSize + getListResult(noDependList, noDependFriendList)
           print "Induced Edges :" + str(inducedEdgeNum)

       print "***Shift Thinning***"
       print "Estimated Size of nodes :" + str(int(totalNodeSize/theta))
   elif breakDep == 2 :
       print "***Safety Margin***"
       print "Estimated Size of nodes :" + str(int(safetymarginIE(sampleList, friendList, theta)))
   else :
       print "Error in breaking dependence type!"

def getListResult(noDependList, noDependFriendList) :
   global sum1JW
   global inducedEdgeNum
   global sumDW
   global sum1W
   global sum1WW
   global sum1EWW
   global sum1JW
   global prevIDegree
   global inducedEdgeNum
   
   sumDW = 0
   sum1W = 0
   sum1WW = 0
   sum1EWW = 0
   sum1JW = 0
   inducedEdgeNum = 0
   
   for [name,degree] in noDependList :
      sum1JW = sum1JW + 1.0/int(degree)
  # print str(sum1JW) + "  qq"

   length = len(noDependList)
   for i in range(0,length) :
      addNode(noDependList[i][0], int(noDependList[i][1]), i, noDependList, noDependFriendList[i])
   return getResult()

def addNode(node, degree, i, sampleList, friendList):
    global sumDW
    global sum1W
    global sum1WW
    global sum1EWW
    global sum1JW
    global prevIDegree
    global inducedEdgeNum

    sum1EW = 0.0

    invDegree = 1.0/degree
    sum1JW = sum1JW - invDegree
    sumDW = sumDW + 1
    sum1W = sum1W + invDegree
    sum1WW = sum1WW + invDegree * sum1JW 

    #'''
    for j in range(i+1, len(sampleList)) :
      if sampleList[j][0]  in friendList:
        sum1EW =  sum1EW + 1.0/int(sampleList[j][1])
        inducedEdgeNum = inducedEdgeNum + 1
    #    print str(sum1EWW) + " " + str(sampleList[j][1]) + " " + str(sampleList[j][0]) + " " + str(i) + " " + str(invDegree)
    sum1EWW = sum1EWW + invDegree * sum1EW
    
 #   if sum1EW != 0 :
 #     print str(degree)+" " + str(1.0/sum1EW)+" "+str(sum1EWW)
    #  '''
   
    


def getResult() :
    global sumDW
    global sum1W
    global sum1WW
    global sum1EWW
    print "sumDW " + str(sumDW)
    print "sum1W " + str(sum1W)
    print "sum1WW " + str(sum1WW)
    print "sum1EWW " + str(sum1EWW)
    return int(sumDW * sum1WW / sum1W / sum1EWW + 1)

def safetymarginIE(sampleList, friendList, hops):
 mysumDW1 = 0.0
 mysum1W1 = 0.0
 length = len(sampleList)
 for i in range(0, length - 1) :
  for j in range(0, length - 1) :
   if abs(i - j) > hops :
    if sampleList[j][0] in friendList[i] :
     mysum1W1 = mysum1W1 + 1 / float(sampleList[i][1])
    mysumDW1 = mysumDW1 + float(sampleList[i][1]) / float(sampleList[j][1])

 return mysumDW1 / mysum1W1
