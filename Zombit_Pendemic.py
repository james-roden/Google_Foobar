# -----------------------------------------------
# Google-Foobar
# Name: Zombit Pandemic
# Level: 5
# Challenge: 1
# Author: James M Roden
# Created: September 2016
# Python Version 2.6
# PEP8
# -----------------------------------------------

"""
Zombit pandemic
===============

The nefarious Professor Boolean is up to his usual tricks. This time he is
using social engineering to achieve his twisted goal of infecting all the
rabbits and turning them into zombits! Having studied rabbits at length, he
found that rabbits have a strange quirk: when placed in a group, each rabbit
nudges exactly one rabbit other than itself. This other rabbit is chosen
with uniform probability. We consider two rabbits to have socialized if either
or both of them nudged the other. (Thus many rabbits could have nudged the same
rabbit, and two rabbits may have socialized twice.)
We consider two rabbits A and B to belong to the same rabbit warren if they
have socialized, or if A has socialized with a rabbit belonging to the same
warren as B.

For example, suppose there were 7 rabbits in Professor Boolean's nefarious lab.
We denote each rabbit using a number.
The nudges may be as follows:

1 nudges 2
2 nudges 1
3 nudges 7
4 nudges 5
5 nudges 1
6 nudges 5
7 nudges 3

This results in the rabbit warrens {1, 2, 4, 5, 6} and {3, 7}.

Professor Boolean realized that by infecting one rabbit, eventually it would
infect the rest of the rabbits in the same warren! Unfortunately, due to budget
 constraints he can only infect one rabbit, thus infecting only the rabbits
in one warren. He ponders, what is the expected maximum number of rabbits he
 could infect?

Write a function answer(n), which returns the expected maximum number of
rabbits Professor Boolean can infect given n, the number of rabbits. n will
be an integer between 2 and 50 inclusive. Give the answer as a string
representing a fraction in lowest terms, in the form "numerator/denominator".
Note that the numbers may be large.

For example, if there were 4 rabbits, he could infect a maximum of 2
(when they pair up) or 4 (when they're all socialized), but the expected
value is 106 / 27. Therefore the answer would be "106/27".

Test cases
==========

Inputs:
    (int) n = 4
Output:
    (string) "106/27"

Inputs:
    (int) n = 2
Output:
    (string) "2/1"

Notes
===============
Wow, this one got real heavy on the maths! Definitely out of my depth
mathematically but my Googling (irony?) skills are on point.

Huge shout out to Jacopo Notarstefano for his elegant maths work
http://math.stackexchange.com/a/1097730/364882

and to David here
http://math.stackexchange.com/questions/1071564/

Binomial Coefficient Multiplicative Formula
https://en.wikipedia.org/wiki/Binomial_coefficient#Multiplicative_formula

Partition
https://en.wikipedia.org/wiki/Partition_(number_theory)

A wonderfully quick partition algorithm by Jermoe Kelleher
http://jeromekelleher.net/generating-integer-partitions.html

EIS
https://oeis.org/A000435
https://oeis.org/A001864

"""

from math import factorial as f
from operator import mul
from fractions import gcd
import time


def timeit(func):
    """
    Timing decorator function
    """

    def timed(*args):
        ts = time.time()
        # Arbitrary range for timing
        for i in xrange(10, 1000):
            func(*args)
        te = time.time()
        return te - ts

    return timed


# Memoization decorator function
def memoize(func):
    """
    Memoization decorator function
    """

    # Memoize dictionary
    mem = {}

    # Wrapper function
    def wrapper(*args):
        if args not in mem:
            mem[args] = func(*args)
        return mem[args]

    return wrapper


# Major issues with float division, lesson learnt. Pseudoforest generated
# from A001864/n instead

@memoize
def pseudoforest(n):
    """
    Returns the number of pseudoforests with all nodes connected by a single tree
    """

    total = 0
    for k in range(1, n):
        total += binomial(n, k) * (n - k) ** (n - k) * k ** k
    return total / n


# My implementation of binomial coefficients
@memoize
def binomial(n, k):
    """
    An efficient multiplicative formula to compute individual binomial coefficients
    """

    ans = 1
    for i in xrange(1, k + 1):
        ans = (ans * (n - (k - i))) / i
    return ans


# Number of ways n labelled items can be split according to partitions
def c(n, partition):
    """
    Returns the number of ways n labelled items can be arranged given the partitions
    Based on formula here:
    http://math.stackexchange.com/a/1097730/364882
    """

    numlist = []
    for i in range(len(partition)):
        numList.append(binomial(n, partition[i]))
        n -= partition[i]
    mulp = [partition.count(p) for p in set(partition)]
    num = reduce(mul, numlist)
    den = reduce(mul, map(f, mulp))
    return num / den


# Generator that creates lists of integer partitions for n
def partitions(n):
    """
    Generates integer partitions for n
    Jerome Kelleher 2014
    http://jeromekelleher.net/generating-integer-partitions.html
    """

    a = [0 for i in range(n + 1)]
    k = 1
    y = n - 1
    while k != 0:
        x = a[k - 1] + 1
        k -= 1
        while 2 * x <= y:
            a[k] = x
            y -= x
            k += 1
        l = k + 1
        while x <= y:
            a[k] = x
            a[l] = y

            # Do not use partition inc one node
            no1 = a[:k + 2]
            if 1 not in no1:
                yield no1

            x += 1
            y -= 1
        a[k] = x + y
        y = x + y - 1

        # Do not use partition inc one node
        no1 = a[:k + 1]
        if 1 not in no1:
            yield no1


# Calculate numerator
def numerator(n):
    """
    Returns the numerator for answer
    Based on formula here:
    http://math.stackexchange.com/a/1097730/364882
    """

    result = 0
    for p in partitions(n):
        result += max(p) * c(n, p) * (reduce(mul, (map(pseudoforest, p))))
    return result


# Answer function
def answer(n):
    """
    Calculates denominator and numerator and reduces fraction to lowest terms
    Returns in string format
    """

    den = (n - 1) ** n
    num = numerator(n)
    div = gcd(num, den)
    return "{}/{}".format(num / div, den / div)

"""
BACK UP FUNCTIONS - NOT USED
"""


# Alternative implementation of pseudoforest
# Psuedoforest equation from https://oeis.org/A000435
# a(n) = (n-1)! * Sum(n^k/k!, k=0..n-2)
# This ultimately fails the Google Foobar test due to float division!
@memoize
def pseudoforest2(n):
    """
    *This ultimately fails due to float division*
    Returns the number of pseudoforests with exactly one connected component
    involving all the nodes, ie. all nodes connected by a single tree
    """
    total = 0
    for k in (range(n - 1)):
        total += (n ** k) / f(k)
    return round(f(n - 1) * total)


# Alternative implementation of binomial coefficients
@memoize
def binomial2(n, k):
    """
    A fast way to calculate binomial coefficients based on Multiplicative formula
    ref. J.F. Sebastian
    http://stackoverflow.com/a/3025547/6779261
    """
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in xrange(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0
