'''
Line up the captives
====================

As you ponder sneaky strategies for assisting with the great rabbit escape, you realize
that you have an opportunity to fool Professor Booleans guards into thinking there are
fewer rabbits total than there actually are.

By cleverly lining up the rabbits of different heights, you can obscure the sudden departure
of some of the captives.

Beta Rabbits statisticians have asked you for some numerical analysis of how this could be
done so that they can explore the best options.

Luckily, every rabbit has a slightly different height, and the guards are lazy and few in
number. Only one guard is stationed at each end of the rabbit line-up as they survey their
captive population. With a bit of misinformation added to the facility roster, you can make
the guards think there are different numbers of rabbits in holding.

To help plan this caper you need to calculate how many ways the rabbits can be lined up such
that a viewer on one end sees x rabbits, and a viewer on the other end sees y rabbits, because
some taller rabbits block the view of the shorter ones.

For example, if the rabbits were arranged in line with heights 30 cm, 10 cm, 50 cm, 40 cm,
and then 20 cm, a guard looking from the left side would see 2 rabbits (30 and 50 cm) while
a guard looking from the right side would see 3 rabbits (20, 40 and 50 cm). 

Write a method answer(x,y,n) which returns the number of possible ways to arrange n rabbits
of unique heights along an east to west line, so that only x are visible from the west, and
only y are visible from the east. The return value must be a string representing the number
in base 10.

If there is no possible arrangement, return "0".

The number of rabbits (n) will be as small as 3 or as large as 40
The viewable rabbits from either side (x and y) will be as small as 1 and as large as the
total number of rabbits (n).

Notes
==================
Mathematically I couldn't quite get to the answer, but a very helpful post by the user Taylan on StackExchange
pointed me in the correct direction:
http://math.stackexchange.com/questions/1849877/


Stirling numbers of the first kind:
https://en.wikipedia.org/wiki/Stirling_numbers_of_the_first_kind
https://sites.google.com/site/ksstirlingnumbers/stirling-numbers-of-the-first-kind

Combinations:

nCr =   n!
      r!(n-r)!

Line up the captives solution formula:

S(n-1, x+y-2) * C(x+y-2, x-1)

Shout out to The Code Ship for help understanding decorators
http://thecodeship.com/patterns/guide-to-python-function-decorators/

'''

from math import factorial as f

# Memoization decorator function
def memoize(func):
    # Memoize Dictionary
    mem_stir = {}
    # Wrapper function
    def wrapper(*args):
        if args not in mem_stir:
            mem_stir[args] = func(*args)
        return mem_stir[args]
    return wrapper


@memoize
def stirling(n,k):

    # There cannot be more cycles than elements
    if k > n:
        return 0

    # There are no ways to arrange n elements in 0 cycles
    elif k == 0 and n >= 1:
        return 0

    # There is only one way to assign n elements into n cycles
    elif k == n and n >= 0:
        return 1
   
    # Return n! as we can arrange n elements in 1 cycle
    elif k == 1 and n >= 1:
        return f(n-1)

    elif k == n-1:
        # All elements have their own cycle except 1 pair
        return combinations(n,2)
    
    # Recursive equation for all other cases
    else:
        return stirling(n-1,k-1) + stirling(n-1, k) * (n-1)


# Combinations function
def combinations(n,r):
    return f(n) / (f(r) * f(n-r))


def answer(x,y,n):

    #Formula: S(n-1, x+y-2) * C(x+y-2, x-1)

    # Solve S
    
    s = stirling(n-1,x+y-2)
      
    # Solve C
    c = combinations(x+y-2,x-1)    
    
    # Return solution (S * C)
    return str(s * c)