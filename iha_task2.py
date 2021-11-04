### SAMPLE POINT CLASS THAT ALSO INCLUDES THE FUNCTION WHICH CALCULATES DISTANCE BETWEEN TWO POINTS

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def find_distance(point1: Point, point2: Point) -> float:
    return (((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2) ** 0.5).__round__(2)



import find_distance


# I use Shoelace formula to calculate the area of a polygon
# here is the source of the formula: https://wikimedia.org/api/rest_v1/media/math/render/svg/198dd2b0bde1ff082dbf02fb1d75c0ad0f5fcec4
### THE POINTS MUST BE IN CLOCKWISE OR COUNTER CLOCKWISE ORDER IF NOT IT WILL NOT WORK
### YOU CAN USE INFINITE POINTS TO MAKE A POLYGON

class Polygon:
    def polygon_area(vertices):
        psum = 0
        nsum = 0
        # if the number of vertices is two , then calculate the distance between the two vertices
        if (len(vertices) == 2):
            return print(
                "You inserted 2 vertices. I will calculate distance between given points instead: " + str(
                    find_distance.find_distance(
                        vertices[0], vertices[1])))
        # the algorithm of the shoelace formula
        for i in range(len(vertices)):
            sindex = (i + 1) % len(vertices)
            prod = vertices[i].x * vertices[sindex].y
            psum += prod

        for i in range(len(vertices)):
            sindex = (i + 1) % len(vertices)
            prod = vertices[i].y * vertices[sindex].x
            nsum += prod

        return print("Area of given points: " + str(abs(1 / 2 * (psum - nsum))))


# test for function find_distance
print("Distance between given two points is: " + str(
    (find_distance.find_distance(find_distance.Point(0, 0), find_distance.Point(1, 1)))))

# if there are two inputs, then it is a distance calculation
two_points = [find_distance.Point(-1, -2), find_distance.Point(1, -2)]
Polygon.polygon_area(two_points)

# check if it is working for non convex polygon
# points of a non convex pentagon
points_non_convex = [find_distance.Point(-1, -2), find_distance.Point(1, -2), find_distance.Point(1, 2),
                     find_distance.Point(0, 0), find_distance.Point(-1, 2)]
Polygon.polygon_area(points_non_convex)

# check if it is working on a triangle
# points of a triangle
points_triangle = [find_distance.Point(-1, -2), find_distance.Point(1, -2), find_distance.Point(0, 0)]
Polygon.polygon_area(points_triangle)

# check if it is working on a square
# points of a square
points_square = [find_distance.Point(-1, -2), find_distance.Point(1, -2), find_distance.Point(1, 2),
                 find_distance.Point(-1, 2)]
Polygon.polygon_area(points_square)

# check if it is working on a pentagon
# points of a pentagon
points_pentagon = [find_distance.Point(-1, -2), find_distance.Point(1, -2), find_distance.Point(1, 2),
                   find_distance.Point(0, 0), find_distance.Point(-1, 2)]
Polygon.polygon_area(points_pentagon)

# check if it is working on a hexagon
# points of a hexagon
points_hexagon = [find_distance.Point(-1, -2), find_distance.Point(1, -2), find_distance.Point(1, 2),
                  find_distance.Point(0, 0), find_distance.Point(-1, 2), find_distance.Point(0, -1)]
Polygon.polygon_area(points_hexagon)

# check if it is working on a heptagon
# points of a heptagon
points_heptagon = [find_distance.Point(-1, -2), find_distance.Point(1, -2), find_distance.Point(1, 2),
                   find_distance.Point(0, 0), find_distance.Point(-1, 2), find_distance.Point(0, -1),
                   find_distance.Point(1, -1)]
Polygon.polygon_area(points_heptagon)

# check if it is working on a octagon
# points of a octagon
points_octagon = [find_distance.Point(-1, -2), find_distance.Point(1, -2), find_distance.Point(1, 2),
                  find_distance.Point(0, 0), find_distance.Point(-1, 2), find_distance.Point(0, -1),
                  find_distance.Point(1, -1), find_distance.Point(1, 1), find_distance.Point(-1, 1)]
Polygon.polygon_area(points_octagon)
