from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f'{self.x}, {self.y}'
        
class Line:
    count = 0
    
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2
        self.c()
               
    def show(self):
        print(self.p1, self.p2)
        
    def lenght(self):
        return sqrt(pow(abs(self.p1.x - self.p2.x), 2) + pow(abs(self.p1.y - self.p2.y), 2))
    
    @classmethod
    def c(cls):
        cls.count += 1
        
    def is_horizontal(self):
        return True if self.p1.x == self.p2.x else False
    
    def is_vertical(self):
        return True if self.p1.y == self.p2.y else False
    
    @staticmethod
    def privet():
        print('zdarova')
        
    
p1 = Point(1, 2)
p2 = Point(3, 4)

l = Line(p1, p2)

l.show()

print(l.lenght())

Line.privet()