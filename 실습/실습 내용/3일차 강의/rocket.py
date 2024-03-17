class Rocket:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f"로켓의 위치 = ({self.x}, {self.y})"

    def moveUp(self):
        self.y += 1
        
    def goto(self, x, y):
        self.x = x
        self.y = y
        
myRocket = Rocket()
print(myRocket)
myRocket.moveUp()
print(myRocket)
myRocket.goto(100, 200)
print(myRocket)
