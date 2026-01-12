class Complex:
    def __init__(self,real,img):
        self._real=real
        self._img=img

    def showNumber(self):
        print(self._real,"i","+",self._img,"j")

    def __add__(self,num2):
        newreal=self._real+num2._real
        newImg=self._img+num2._imgQ
        return Complex(newreal,newImg)

num1=Complex(1,3)
num1.showNumber()

num2=Complex(4,6)
num2.showNumber()

num3=num1+num2
num3.showNumber()