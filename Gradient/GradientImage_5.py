def mkArray():
	x = []
	tmp=0
	for n in range(0, 500):
		tmp += 1
		if tmp % 150 == 0:
			x.append(tmp)
		else:
			x.append(0)
	return x

biga = []

for n in range(0, 500):
	biga.append(mkArray())

def ArrayToString(arr):
	tmp = ""
	for i in arr:
		tmp += str(i) + " "
	return tmp

def mkFile():
	myf = open("test9.pgm","w")
	myf.write("P2\n500 500\n255\n")
	for n in biga:
		myf.write(ArrayToString(n))
	myf.close()

mkFile()
