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

def mkHLine(array, row, start, stop):
	for n in range(len(array[row])):
			if n >= start and n <= stop:
				array[row][n] = 1
	return array

def mkVLine(array, col, start, stop):
	for n in array:
		for m in n:
			if m > start and m < stop:
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

def Rectangle(img, row1, row2, col1, col2, start1, stop1):
	mkHLine(img, row1, start1, stop1)
	mkHLine(img, row2, start1, stop1)
	mkVLine(img, col1, start1, stop1)
	mkVLine(img, col2, start1, stop1)

image1 = mkArray()

Rectangle(image1, 3, 95, 3, 95, 3, 95)
##Rectangle(image1, 15, 65, 10, 75, 5, 95)
##Rectangle(image1, 20, 90, 20, 90, 5, 95)

makeFile(image1)
