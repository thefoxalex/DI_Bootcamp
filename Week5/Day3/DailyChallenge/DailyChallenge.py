import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    @property
    def area(self):
        return math.pi * (self.radius ** 2)

    def __str__(self):
        return f"Circle(radius={self.radius:.2f}, diameter={self.diameter:.2f}, area={self.area:.2f})"

    def __repr__(self):
        return f"Circle({self.radius})"

    def __add__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return Circle(self.radius + other.radius)

    def __lt__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius < other.radius

    def __gt__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius > other.radius

    def __eq__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius == other.radius

c1 = Circle(5)   
c2 = Circle(10)     
c3 = Circle(2)     
c4 = Circle(1)
  

print(f"\nArea of largest circle (c2): {c2.area:.2f}")
print(f"Is c2 > c4? {c2 > c4}")      
print(f"Is c1 == c3? {c1 == c3}")   

c5 = c1 + c3
print(f"c1 + c3 = {c5}")            


circles = [c1, c2, c3, c4, c5]
circles.sort()
print("\nSorted list (by radius):")
print(circles)



