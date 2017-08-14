# -----------------------------------------------
# Google-Foobar
# Name: Peculiar Balance
# Level: 2
# Challenge: 2
# Author: James M Roden
# Created: August 2016
# Python Version 2.6
# PEP8
# -----------------------------------------------

"""
Peculiar balance
==========
Can we save them? Beta Rabbit is trying to break into a lab that contains the
only known zombie cure - but there's an obstacle. The door will only open if a
challenge is solved correctly. The future of the zombified rabbit population is
at stake, so Beta reads the  challenge: There is a scale with an object on the
left-hand side, whose mass is given in some number of units.
Predictably, the task is to balance the two sides.
But there is a catch: You only have this peculiar weight set,
having masses 1, 3, 9, 27, ... units. That is, one for each power of 3.
Being a brilliant mathematician, Beta Rabbit quickly discovers that any number
of units of mass can be balanced exactly using this set. To help Beta get into
the room, write a method called answer(x), which outputs a list of strings
representing where the weights should be  placed, in order for the two sides to
be balanced, assuming that weight on the left has mass x units.
The first element of the output list should correspond to the 1-unit weight,
the second element to the 3-unit weight, and so on. Each string is one of:
"L" : put weight on left-hand side
"R" : put weight on right-hand side
"-" : do not use weight
To ensure that the output is the smallest possible, the last element of the list
must not be "-". x will always be a positive integer, no larger than 1000000000.
==========

Test cases
==========
Inputs:
    int(x) = 2
Output:
    str(["L", "R"])
Inputs:
    int(x) = 8
Output:
    str(["L", "-", "R"])

Notes
==========
We can use balanced ternary to get the desired output.
Balanced Ternary (bt) is a representation for numbers. In bt 'digits' are
1, 0, and -1.

 n | 81 | 27 |  9 |  3 |  1 |
   --------------------------
 6 |  0 |  0 |  1 | -1 |  0 | (9, -3, 0 == 6)
 7 |  0 |  0 |  1 | -1 |  1 | (9, -3, 1 == 7)
 8 |  0 |  0 |  1 |  0 | -1 | (9, 0, -1 == 8)
 42|  1 | -1 | -1 | -1 |  0 | (81, -27, -9, -3, 0 == 42)

From this we can see a pattern emerge. In layman's...
n + (all 'negative' values) == (all 'positive' values)
We now know which side each 'weight' has to be placed given n.

Firstly we need to convert the decimal number to ternary. In order to do this
we can use divide/modulo.

E.g.
11 % 3 = 2 .. 11 / 3 = 3
3 % 3 = 0 .. 3 / 3 = 1
1 % 3 = 1 .. 1 / 3 = 0

This gives us the ternary number 1 0 2. Which is (1*9 + 0*3 + 2*1) = 11!
But we need to convert this to balanced ternary. In balanced ternary we
represent a 2 with a -1 in the current place and add +1 in the next higher
place. So instead of 1 0 2, eleven would be 1 1 -1 (1*9 + 1*3 + -1*1) = 11!
"""


def answer(x):
    """
    As specified
    """

    if x == 0:
        return 0
    nums = []
    while x:
        # Convert decimal to ternary
        r = x % 3
        x = x / 3
        # Convert ternary to balanced ternary
        if r == 2:
            r = -1
            x += 1
        nums.append(r)
    weights = []
    # Iterate through balanced ternary and change to desired string
    for num in nums:
        weights.append(["-", "R", "L"][num])
    return weights 
