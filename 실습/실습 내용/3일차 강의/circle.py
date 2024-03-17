import math

class Circle:
    def __init__(self, radius):
        self.r = radius
        
    def getArea(self):
        return math.pi * self.r ** 2
    
    def getPerimeter(self):
        return 2 * math.pi * self.r
    
c = Circle(10)
print(f"원의 면적 = {c.getArea()}")
print(f"원의 둘레 = {c.getPerimeter()}")