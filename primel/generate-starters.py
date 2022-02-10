import sympy

"""
Generates a prime number with five unique digits.
@wantedDigits Only print if it features digits included in this set. Digits must be as strings. Empty set by default.
@unwantedDigits Only print if it DOES NOT feature digits included in this set. Digits must be as strings. Empty set by default.

Example usages:
generateStarter()
generateStarter({'1'})
generateStarter({'8', '7', '0,'})
generateStarter(set("123"))
generateStarter(set("239"), set("17"))

"""

def generateStarter(wantedDigits=set({}), unwantedDigits=set({})):

    # brute-force check all 5-digit primes (not very efficient as of now)
    for i in sympy.primerange(10000, 100000):

        gen = set(str(i))

        # print if all digits are unique
        if len(gen) == 5 and wantedDigits.issubset(gen) and unwantedDigits.isdisjoint(gen):
            print(i, end=", ")