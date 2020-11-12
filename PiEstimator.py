# given points randomly allocated in a square
# write a program to estimate pi
import random
import math
# first we need to get a function to randomly create points
random.uniform(0, 1)

# creates a new point
def new_point():
    x = random.uniform(0, 1)
    y = random.uniform(0, 1)
    return x, y


# creates a specified number of points
def create_points(num_points):
    points = []
    for n in range(num_points):
        x, y = new_point()
        points.append((x, y))
    return points


# this function will estimate the value of pi using points
# also using area = pi * r**2
def estimate_pi(num_points):
    points = create_points(num_points)
    inside = 0
    total = 0
    for i in range(len(points)):
        if inside_circle(points[i]):
            inside = inside + 1
            total = total + 1
        else:
            total = total + 1
    # area/4 = (pi * r**2)/4
    # lots of cancelling but because our radius is 1, there is no effect
    # so we basically multiply our ratio by 4 to get whole circle
    pi = inside/total * 4
    print("Pi estimated to: " + str(pi))



# this function will count whether the point is <= 1 away from the origin
def inside_circle(point):
    if math.sqrt(point[0]**2 + point[1]**2) <= 1:
        return True
    else:
        return False


def get_number_points():
    try:
        value = int(input("Type a number:"))
        return value
    except ValueError:
        print("This is not a whole number.")
        value = get_number_points()
        return value


if __name__ == "__main__":
    number_points = get_number_points()
    estimate_pi(number_points)
