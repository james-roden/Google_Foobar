'''
Carrotland
==========

The rabbits are free at last, free from that horrible zombie science experiment. They need a happy,
safe home, where they can recover. 

You have a dream, a dream of carrots, lots of carrots, planted in neat rows and columns! But first,
you need some land. And the only person who's selling land is Farmer Frida. Unfortunately, not only
does she have only one plot of land, she also doesn't know how big it is - only that it is a triangle.
However, she can tell you the location of the three vertices, which lie on the 2-D plane and have
integer coordinates.

Of course, you want to plant as many carrots as you can. But you also want to follow these guidelines:
The carrots may only be planted at points with integer coordinates on the 2-D plane. They must lie
within the plot of land and not on the boundaries. For example, if the vertices were
(-1,-1), (1,0) and (0,1), then you can plant only one carrot at (0,0).

Write a function answer(vertices), which, when given a list of three vertices, returns the maximum
number of carrots you can plant.

The vertices list will contain exactly three elements, and each element will be a list of two
integers representing the x and y coordinates of a vertex. All coordinates will have absolute value
no greater than 1000000000. The three vertices will not be collinear.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int) vertices = [[2, 3], [6, 9], [10, 160]]
Output:
    (int) 289

Inputs:
    (int) vertices = [[91207, 89566], [-88690, -83026], [67100, 47194]]
Output:
    (int) 1730960165


Notes
==========
Pick's Theorem:
Given a simple polygon constructed on a grid of equal-distanced points (i.e.
integer coordinates) such that all the polygon vertices are grid points, Pick's
theorem provides a simple formula for calculating the area of the polygon
in terms of i (interior) and b (on boundary) lattice points.

(https://en.wikipedia.org/wiki/Pick%27s_theorem)

Area = i + b/2 - 1

Pick's Theorem rearranged to get lattice points inside triangle:

i = Area - (b/2) + 1


Area of triangle (coordinate geometry) using shoelace formula:

Area = 0.5 * (Ax - Cx) * (By - Ay) - (Ax - Bx) * (Cy - Ay)

(http://en.wikipedia.org/wiki/Shoelace_formula)


Count lattice points on a line (b):

gcd(Bx-Ax, By-Ay) + 1

(Hagen von Eitzen @ math.stackexchange.com)

'''

def answer(vertices):
    # Import gcd
    from fractions import gcd

    # Extract points
    pnt_a = vertices[0]
    pnt_b = vertices[1]
    pnt_c = vertices[2]

    # Area
    area = .5*abs( (pnt_a[0]-pnt_c[0]) * (pnt_b[1]-pnt_a[1]) - (pnt_a[0]-pnt_b[0]) * (pnt_c[1]-pnt_a[1]) )

    # Boundary lattice points
    b_lattices = (gcd(abs(pnt_b[0]-pnt_a[0]), abs(pnt_b[1]-pnt_a[1]))
                  + gcd(abs(pnt_c[0]-pnt_b[0]),abs(pnt_c[1]-pnt_b[1]))
                  + gcd(abs(pnt_a[0]-pnt_c[0]),abs(pnt_a[1]-pnt_c[1])))

    # Pick's Theorem
    i_lattices = area - (b_lattices/2) + 1
       
    return int(i_lattices)
