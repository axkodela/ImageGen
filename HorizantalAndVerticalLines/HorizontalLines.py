def mkArray(value):
	x = []
	for n in range(0,100):
		x.append(value)
	return x

biga = []
RowOfBlack = 42
for x in range(0,100):
	if x == RowOfBlack:
		biga.append(mkArray(0))
	else:
		biga.append(mkArray(1))

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
