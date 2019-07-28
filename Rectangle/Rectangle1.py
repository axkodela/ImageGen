imgw = 100
imgh = 100

def mkArray():
	biga = []
	for n in range(0, imgh):
		x = []
		for m in range(0, imgw):
			x.append(0)
		biga.append(x)
	return biga

def mkHLine(array, row):
	for n in range(len(array[row])):
		array[row][n] = 1
	return array

def mkVLine(array, col):
	for n in array:
		n[col] = 1
	return array

def ArrayToString(arr):
	tmp = ""
	for i in arr:
		tmp += str(i) + " "
	return tmp

def makeFile(imgFile):
	myf = open("RectangleImge.pbm", "w")
	myf.write("P1\n"+str(imgh)+" "+str(imgw)+"\n")
	for i in imgFile:
		myf.write(ArrayToString(i))
	myf.close()

def Rectangle(img, row1, row2, col1, col2):
	mkHLine(img, row1)
	mkHLine(img, row2)
	mkVLine(img, col1)
	mkVLine(img, col2)

image1 = mkArray()
Rectangle(image1, 5, 85, 5, 85)
Rectangle(image1, 15, 65, 10, 75)
Rectangle(image1, 20, 90, 20, 90)
makeFile(image1)
