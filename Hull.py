#  File: Hull.py

#  Description:

#  Student Name: Vaishnavi Sathiyamoorthy

#  Student UT EID: vs25229

#  Course Name: CS 313E

#  Unique Number: 52530

#  Date Created: 09/21/2022

#  Date Last Modified:

import sys

import math

class Point (object):
  # constructor
  def __init__(self, x = 0, y = 0):
    self.x = x
    self.y = y

  # get the distance to another Point object
  def dist (self, other):
    return math.hypot (self.x - other.x, self.y - other.y)

  # string representation of a Point
  def __str__ (self):
    return '(' + str(self.x) + ', ' + str(self.y) + ')'

  # equality tests of two Points
  def __eq__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

  def __ne__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) >= tol) or (abs(self.y - other.y) >= tol))

  def __lt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y < other.y)
    return (self.x < other.x)

  def __le__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y <= other.y)
    return (self.x <= other.x)

  def __gt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y > other.y)
    return (self.x > other.x)

  def __ge__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y >= other.y)
    return (self.x >= other.x)

# Input: p, q, r are Point objects
# Output: compute the determinant and return the value
def det (p, q, r):
    # values between 2 determinants are subtracted for each point
    return (q.x * r.y - r.x * q.y) - (p.x * r.y - r.x * p.y) + (p.x * q.y - q.x * p.y)

# Input: sorted_points is a sorted list of Point objects
# Output: computes the convex hull of a sorted list of Point objects
#         convex hull is a list of Point objects starting at the
#         extreme left point and going clockwise in order
#         returns the convex hull
def convex_hull (sorted_points):
    # empty upper hull is created. The first 2 points from the sorted list are added
    upper_hull = []
    upper_hull.append(sorted_points[0])
    upper_hull.append(sorted_points[1])

    # each point from sorted point is added to upper hull. If the value of the determinant is 0 or positive, the second value from the hull is removed
    for i in range(2, len(sorted_points)):
        upper_hull.append(sorted_points[i])
        while len(upper_hull) >= 3:
            if (det(upper_hull[len(upper_hull)-3], upper_hull[len(upper_hull)-2], upper_hull[len(upper_hull)-1]) >= 0):
                del upper_hull[-2]
            else:
                break

    # empty lower hull is created. The first 2 points from the sorted list are added
    lower_hull = []
    lower_hull.append(sorted_points[-1])
    lower_hull.append(sorted_points[-2])

    # each point from sorted point is added to lower hull in reverse order. If the value of the determinant is 0 or positive, the second value from the hull is removed
    for i in reversed(range(0, len(sorted_points)-2)):
        lower_hull.append(sorted_points[i])
        while len(lower_hull) >= 3:
            if (det(lower_hull[len(lower_hull) - 3], lower_hull[len(lower_hull) - 2],
                    lower_hull[len(lower_hull) - 1]) >= 0):
                del lower_hull[-2]
            else:
                break

    # duplicate values are removed
    lower_hull.remove(lower_hull[0])
    lower_hull.remove(lower_hull[len(lower_hull) - 1])

    # upper and lower hull are combined
    convex_hull = []
    for i in range(len(upper_hull)):
        convex_hull.append(upper_hull[i])
    for i in range(len(lower_hull)):
        convex_hull.append(lower_hull[i])
    return convex_hull

# Input: convex_poly is  a list of Point objects that define the
#        vertices of a convex polygon in order
# Output: computes and returns the area of a convex polygon
def area_poly (convex_poly):
    area = 0
    # area = area + abs(x1y2 - x2y1)
    for i in range(len(convex_poly)):
        if i == (len(convex_poly) - 1):
            area += abs((convex_poly[i].x * convex_poly[0].y) - (convex_poly[0].x * convex_poly[i].y))
        else:
            area += abs((convex_poly[i].x * convex_poly[i+1].y) - (convex_poly[i+1].x * convex_poly[i].y))
    # area = 0.5 * area
    return area * 0.5

# Input: no input
# Output: a string denoting all test cases have passed
def test_cases():
  # write your own test cases
  assert det(Point(0,2), Point(0,3), Point(0,4)) == 0
  assert area_poly([Point(0,0), Point(2,0), Point(2,2), Point(0,2)]) == 4


  return "all test cases passed"

def main():
  # create an empty list of Point objects
  points_list = []

  # read number of points
  line = sys.stdin.readline()
  line = line.strip()
  num_points = int (line)

  # read data from standard input
  for i in range (num_points):
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    x = int (line[0])
    y = int (line[1])
    points_list.append (Point (x, y))

  # sort the list according to x-coordinates
  sorted_points = sorted (points_list)


# print the sorted list of Point objects


  # get the convex hull
  print("Convex Hull")
  lst = convex_hull(sorted_points)
  for p in lst:
      print(str(p))
  print()
  print("Area of Convex Hull = " + str(area_poly(lst)))
  # run your test cases
  test_cases()
  # print your results to standard output

  # print the convex hull

  # get the area of the convex hull

  # print the area of the convex hull

if __name__ == "__main__":
  main()