# -----------------------------------------------
# Google-Foobar
# Name: Minions Bored Game
# Level: 4
# Challenge: 4
# Author: James M Roden
# Created: August 2016
# Python Version 2.6
# PEP8
# -----------------------------------------------

"""
Minion's bored game
===================

There you have it. Yet another pointless "bored" game created by the bored
minions of Professor Boolean.

The game is a single player game, played on a board with n squares in a
horizontal row. The minion places a token on the left-most square and rolls
a special three-sided die.

If the die rolls a "Left", the minion moves the token to a square one space to
the left of where it is currently. If there is no square to the left, the game is
invalid, and you start again.

If the die rolls a "Stay", the token stays where it is. 

If the die rolls a "Right", the minion moves the token to a square, one space to
the right of where it is currently. If there is no square to the right, the game
is invalid and you start again.

The aim is to roll the dice exactly t times, and be at the rightmost square on
the last roll. If you land on the  rightmost square before t rolls are done
then the only valid dice roll is to roll a "Stay". If you roll anything else,
the game is invalid (i.e., you cannot move left or right from the rightmost
square).

To make it more interesting, the minions have leaderboards (one for each n,
t pair) where each minion submits the game he  just played: the sequence of
dice rolls. If some minion has already submitted the exact same sequence, they
cannot submit  a new entry, so the entries in the leader-board correspond to
unique games playable.

Since the minions refresh the leaderboards frequently on their mobile devices,
as an infiltrating hacker, you are interested in knowing the maximum
possible size a leaderboard can have.

Write a function answer(t, n), which given the number of dice rolls t, and the
number of squares in the board n, returns  the possible number of unique
games modulo 123454321. i.e. if the total number is S, then return the
remainder upon dividing S by 123454321, the remainder should be an integer
between 0 and 123454320 (inclusive).

n and t will be positive integers, no more than 1000. n will be at least 2.

Test cases
==========

Inputs:
    (int) t = 1
    (int) n = 2
Output:
    (int) 1

Inputs:
    (int) t = 3
    (int) n = 2
Output:
    (int) 3


Notes
===========

Recurrence formula adopted from Juan Lopes
http://stackoverflow.com/questions/29837067/

M(0, 1) = 1
M(t, n) = T(t-1, n-1) + T(t-1, n) + T(t-1, n+1)

Traverse through decision tree using (position left (p-1), position stay (p),
and position right (p+1). When a base case is reached, either return 0 or 1
to represent an invalid or valid game respectively. Return sum of valid games.
Use mod 123454321 on each iteration to prevent integer overflow, as requested
by the problem.
"""


def answer(t, n):
    """
    As required
    """
    # Pre defined mod
    mod = 123454321

    # Memoization dictionary
    mem = {}

    # Recursive function
    def routes(t, p):

        # Store arguments for memoization
        args = t, p
        
        # Check if arguments are already in dictionary
        if args in mem:
            return mem[args]

        # Base cases
        # Prevent moving left if position 1 or
        # not enough turns to reach end
        elif p < 1 or t < n - p:
            return 0        

        # Prevent moving right if position n or 
        # only enough turns to reach end with right moves
        elif p == n or t == n - p:
            return 1
                
        # Recursion of possible routes
        else:
            ans = routes(t - 1, p - 1) + routes(t - 1, p) + routes(t - 1,
                                                                   p + 1) % mod
            # Store answer for memoization
            mem[args] = ans
            return ans

    return routes(t, 1)
