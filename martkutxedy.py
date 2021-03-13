class Martkutxedi:
    def __init__(self,width,length):
        self.width=width
        self.length=length
    def area(self):
        return self.width * self.length
    def perimeter(self):
        return 2*(self.width + self.length)
    def print_info(self):
        print("area:",abcd.area(),"","perimeter",abcd.perimeter(),"",'sigrdze:',self.width,"","sigane",self.length)


abcd= Martkutxedi(3,4)
abcd.print_info()
