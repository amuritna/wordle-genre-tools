import sympy

# argument: set, empty by default, in strings
def generateStarter(wantedDigits={}):

    # no specific wanted digits
    if len(wantedDigits) == 0:

        # brute-force check all 5-digit primes (not very efficient as of now)
        for i in sympy.primerange(10000, 100000):

            # print if all digits are unique
            if len(set(str(i))) == 5:
                print(i)
    
    else:

        # same case as above
        for i in sympy.primerange(10000, 100000):

            gen = set(str(i))

            if len(gen) == 5 and wantedDigits.issubset(gen):
                print(i)

# example usages:
# generateStarter()
# generateStarter({'1'})
# generateStarter({'8', '7', '0', '1'})