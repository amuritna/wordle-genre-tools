import sympy

"""
Generates a prime number with five unique digits.
@wantedDigits Only print if it features digits included in this set. Digits must be as strings. Empty set by default.

Example usages: generateStarter(), generateStarter({'1'}), generateStarter({'8', '7', '0,'}), generateStarter(set("123"))
"""
def generateStarter(wantedDigits={}):

    # no specific wanted digits
    if len(wantedDigits) == 0:

        # brute-force check all 5-digit primes (not very efficient as of now)
        for i in sympy.primerange(10000, 100000):

            # print if all digits are unique
            if len(set(str(i))) == 5:
                print(i, end=", ")
    
    else:

        # same case as above
        for i in sympy.primerange(10000, 100000):

            gen = set(str(i))

            if len(gen) == 5 and wantedDigits.issubset(gen):
                print(i, end=", ")