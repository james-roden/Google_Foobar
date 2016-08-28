'''
Breeding like rabbits
=====================

As usual, the zombie rabbits (zombits) are breeding... like rabbits! But instead of following the Fibonacci
sequence like all good rabbits do, the zombit population changes according to this bizarre formula, where R(n)
is the number of zombits at time n:

R(0) = 1
R(1) = 1
R(2) = 2
R(2n) = R(n) + R(n + 1) + n (for n > 1)
R(2n + 1) = R(n - 1) + R(n) + 1 (for n >= 1)

(At time 2, we realized the difficulty of a breeding program with only one zombit and so added an additional zombit.)

Being bored with the day-to-day duties of a henchman, a bunch of Professor Boolean's minions passed the time by playing
a guessing game: when will the zombit population be equal to a certain amount? Then, some clever minion objected that
this was too easy, and proposed a slightly different game: when is the last time that the zombit population will be equal
to a certain amount? And thus, much fun was had, and much merry was made.

(Not in this story: Professor Boolean later downsizes his operation, and you can guess what happens to these minions.)

Write a function answer(str_S) which, given the base-10 string representation of an integer S, returns the largest n such
that R(n) = S. Return the answer as a string in base-10 representation. If there is no such n, return "None". S will be a
positive integer no greater than 10^25.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (string) str_S = "7"
Output:
    (string) "4"

Inputs:
    (string) str_S = "100"
Output:
    (string) "None"


Notes
==========

Recursive sequences
http://www.theproblemsite.com/reference/mathematics/algebra/sequences-and-series/recursive-sequences



    
'''

def answer(str_S):

    # Memoization dictionary
    rabbits = {0:1, 1:1, 2:2}

    # Recursive function
    def r(n):        
        
        # Check memoized values
        if n not in rabbits:

            # Even recursive sequence
            if n % 2 == 0:
                h = n/2
                rabbits[n] =  r(h) + r(h + 1) + h
                return rabbits[n]
                    
            # Odd recurisve sequence 
            elif n % 2 == 1:
                h = (n-1)/2
                rabbits[n] = r(h - 1) + r(h) + 1
                return rabbits[n]

        return rabbits[n]

    # Binary search function.
    def binary_search(inc,zombits):
        lower = 0
        upper = zombits + 1

        while lower < upper:
            mid = (upper+lower)/2

            # Either run on odd or even numbers
            if inc == 1:
                if mid % 2 == 0:
                    mid += 1
            elif inc == 0:
                if mid % 2 == 1:
                    mid +=1
            
            guess = r(mid)            

            if guess == zombits:
                return mid
            elif guess < zombits:
                lower = mid+1
            elif guess > zombits:
                upper = mid-1
                
        return None

    # Convert string to int
    zombits_n = int(str_S,10)
    
    # Binary search even numbers
    even = binary_search(0, zombits_n)
    
    # Binary search odd numbers
    odd = binary_search(1, zombits_n)

    # Return None if zombits_n is in neither binarys search
    if even is None and odd is None:
        answer = "None"
    
    # Else, return max value
    else:
        answer = max(even,odd)
    
    # Convert back to string
    return str(answer)