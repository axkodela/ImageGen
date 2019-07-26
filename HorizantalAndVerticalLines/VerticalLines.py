def mkArray(value):
	x = []
	for n in range(0,100):
		if n == value:
			x.append(1)
		else:
			x.append(0)
	return x

biga = []
for x in range(0,100):
	biga.append(mkArray(45))

def ArrayToString(arr):
	tmp = ""
	for i in arr:
		tmp += str(i) + " "
	return tmp

def mkFile():
	myf = open("Horizontal.pbm","w")
	myf.write("P1\n100 100\n")
	for n in biga:
		myf.write(ArrayToString(n))
	myf.close()

mkFile()
