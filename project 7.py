print("name:T P Aswathi\n","sec:o\n","usn:1AY24AI109")
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, corner, width, height):
        self.corner = corner
        self.width = width
        self.height = height
class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

def point_in_circle(circle, point):
    dx = point.x - circle.center.x
    dy = point.y - circle.center.y
    distance = math.hypot(dx, dy)
    return distance <= circle.radius
def rect_in_circle(circle, rect):

    corners = [
        rect.corner,
        Point(rect.corner.x + rect.width, rect.corner.y),
        Point(rect.corner.x, rect.corner.y + rect.height),  
        Point(rect.corner.x + rect.width, rect.corner.y + rect.height)  
    ]
    return all(point_in_circle(circle, corner) for corner in corners)


def rect_circle_overlap(circle, rect):

    corners = [
        rect.corner,
        Point(rect.corner.x + rect.width, rect.corner.y),
        Point(rect.corner.x, rect.corner.y + rect.height),
        Point(rect.corner.x + rect.width, rect.corner.y + rect.height)
    ]
    for corner in corners:
        if point_in_circle(circle, corner):
            return True

    return False
center_point = Point(150, 100)
circle = Circle(center=center_point, radius=75)

p = Point(160, 110)
print("Point in Circle:", point_in_circle(circle, p))
rect = Rectangle(Point(120, 80), 50, 30)
print("Rectangle in Circle:", rect_in_circle(circle, rect))

print("Rectangle overlaps Circle:", rect_circle_overlap(circle, rect))
