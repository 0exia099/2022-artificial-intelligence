class Vector2D:
    def __init__(self, x, y) :
        self.x = x
        self.y = y
        
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __repr__(self):
        return f"({self.x}, {self.y})"
    
    def __add__(self, other):
        return Vector2D(self.x+other.x, self.y+other.y)
    
    def __sub__(self, other):
        return Vector2D(self.x-other.x, self.y-other.y)
    
    def __gt__(self, other):
        return self.x**2 + self.y**2 > other.x**2 + other.y**2
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
u = Vector2D(0,1)
v = Vector2D(1,0)
a = u + v
c = u - v
d = a - c
A = [d, c, u, v, a]
B = sorted(A)
print(a)
print(A)
print(B)
print(A == B)
