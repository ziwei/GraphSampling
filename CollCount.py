import depend

visitedNodes = set()
collision = 0
sumDegree = 0
sumRDegree = 0
estimateNodeSize = 0

def collisionCount(sampleList,breakDep,theta) :
	print "+++Collision Counting+++"
	noDependList = []
	if breakDep == 0 :
		noDependList = depend.thinningsample(sampleList,theta,0)
		#print noDependList[3][1]
		print "***Simple Thinning***"
		print "Estimated Size of nodes :" + str(getListResult(noDependList))
	elif breakDep == 1 :
		totalNodeSize = 0
		for i in range(0,theta-1) :
			noDependList = depend.thinningsample(sampleList,theta,i)
			totalNodeSize = totalNodeSize + getListResult(noDependList)
		print "***Shift Thinning***"
		print "Estimated Size of nodes :" + str(int(totalNodeSize/theta))
	elif breakDep == 2 :
		print "***SaftyMargin***"
		print "Estimated Size of nodes :" + str(int(safetyMargin(sampleList,theta)))
	else :
		 print "Error in breaking dependence type!"

def getListResult(noDependList) :
	for [name,degree] in noDependList :
		#print name + " " + degree
		addNode(name, int(degree))
	return getResult()

def addNode(node, degree):
   	global collision
   	global visitedNodes
   	global sumDegree
   	global sumRDegree
   	if node in visitedNodes :
   		collision = collision + 1
		#print visitedNodes
   	else :
   		visitedNodes.add(node) 
     
   	#print visitedNodes
   	sumDegree = sumDegree + degree
   	sumRDegree = sumRDegree + 1.0/degree

def getResult() :
    	global collision
    	global sumDegree
    	global sumRDegree
	if collision == 0 :
	 collision = 1
    	return  sumDegree * sumRDegree *0.5 /collision
    
def printResult():
    	global visitedNodes
    	global collision
    	global sumDegree
    	global sumRDegree
    	print "Size of Set:" + str(len(visitedNodes))
    	print "Collision:" + str(collision)
    	print "Estimated Number:" + str(sumDegree * sumRDegree *0.5 /collision)

def safetyMargin(sampleList,delta) :
   length = len(sampleList)
   sumUp = 0.0
   sumDown = 0.0
   for i in range(0,length) :
       iDegree = sampleList[i][1]
       iName = sampleList[i][0]
       for j in range(0,length) :
           if abs(j-i)>delta :
               sumUp = sumUp + float(iDegree)/float(sampleList[j][1])
               if iName == sampleList[j][0] :
                   sumDown = sumDown + 1

   result = sumUp/sumDown
   return result


