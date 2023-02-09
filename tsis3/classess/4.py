import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(self.x, self.y)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def dist(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

p1 = Point(1, 2)
p2 = Point(3, 4)


print("Point 1:")
p1.show()

p2.move(-2, 3)
print("Point 2 after move function:")
p2.show()

print("Distance between two points")
print(p1.dist(p2))

