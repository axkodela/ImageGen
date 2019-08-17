def mkArrayfront():
	biga = []
	currpos = 0
	for n in range(0,10):
		x = []
		for m in range(0,10):
			if m == currpos:
				x.append(1)
			else:
				x.append(0)
		currpos+=1
		biga.append(x)
	return biga

def mkArrayback():
	biga = []
	currpos = 10
	for n in range(10):
		x = []
		for m in range(10):
			if m == currpos:
				x.append(1)
			else:
				x.append(0)
		currpos-=1
		biga.append(x)
	return biga

def ArrayToString(arr):
	tmp = ""
	for i in arr:
		tmp += str(i) + " "
	return tmp

def mkFile(fname):
	myf = open(fname,"w")
	myf.write("P1\n10 10\n")
	for n in biga:
		myf.write(ArrayToString(n))
	myf.close()

biga = mkArrayfront()
mkFile("DiagonalsF.pbm")
biga = mkArrayback()
mkFile("DiagonalsB.pbm")
