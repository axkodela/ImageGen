h = 100
w = 100

def mkArray():
	global h,w
	biga = []
	for n in range(h):
		x = []
		for n in range(w):
			x.append(0)
		biga.append(x)
	return biga

def modArray(array):
	counter = 0
	for n in range(len(array)):
		array[n][counter] = 1
		counter+=1
	return array

def modArrayBackwards(array):
	counter = len(array[0])-1
	for n in range(len(array)-1):
		array[n][counter] = 1
		counter-=1
	return array

def ArrayToString(arr):
	tmp = ""
	for i in arr:
		tmp += str(i) + " "
	return tmp

def mkFile(fname,mya):
	myf = open(fname,"w")
	myf.write("P1\n"+ str(h) + " " + str(w) +"\n")
	for n in mya:
		myf.write(ArrayToString(n))
	myf.close()

x = mkArray()
y = modArray(x)
z = modArrayBackwards(y)
mkFile("Diagonal.pbm", z)
