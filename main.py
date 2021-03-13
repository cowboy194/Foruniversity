class Calculator:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def mimateba(self):
        return  self.x + self.y
    def gamokleba(self):
        return self.x - self.y
    def gamravleba(self):
        return self.x * self.y
    def gayofa(self):
        return self.x/self.y





num1 =int(input('x:'))
num2 =int(input('y:'))
numbers = Calculator(num1,num2)
print("jami",numbers.mimateba())
print("sxvaoba",numbers.gamokleba())
print("namravli",numbers.gamravleba())
print("ganayofi",numbers.gayofa())