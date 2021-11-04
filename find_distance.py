### SAMPLE POINT CLASS THAT ALSO INCLUDES THE FUNCTION WHICH CALCULATES DISTANCE BETWEEN TWO POINTS

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def find_distance(point1: Point, point2: Point) -> float:
    return (((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2) ** 0.5).__round__(2)


