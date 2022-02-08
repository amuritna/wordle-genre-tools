from random import randrange
import sympy

# string keys because we'll be iterating through strings later
digitCount = dict([(str(i), 0) for i in range(10)])

# dictionary of dicts
digitDistribution = dict(
        [
            (
                str(i), 
                dict([(str(i), 0) for i in range(10)])
            )
        for i in range(5)]
    )

counter = 0

# iterate through all 5-digit primes (assumption: no zeroes at the beginning of the number)
for i in sympy.primerange(10000, 100000):
    stringified = str(i)

    for j in range(5):
        digitCount[stringified[j]] += 1
        digitDistribution[str(j)][stringified[j]] += 1

    counter += 1

print("\nOccurence of each digit:\n")
print(digitCount)
print("\n\nDistribution of each digit:\n")
print(digitDistribution)
print(f'\nFound {counter} eligible primes.\n')

"""
RESULT:

Occurence of each digit:

{'0': 2493, '1': 5672, '2': 3515, '3': 5552, '4': 3412, '5': 3456, '6': 3372, '7': 5520, '8': 3339, '9': 5484}


Distribution of each digit:

{'0': {'0': 0, '1': 1033, '2': 983, '3': 958, '4': 930, '5': 924, '6': 878, '7': 902, '8': 876, '9': 879}, '1': {'0': 839, '1': 856, '2': 870, '3': 832, '4': 822, '5': 846, '6': 826, '7': 847, '8': 788, '9': 837}, '2': {'0': 822, '1': 857, '2': 815, '3': 825, '4': 846, '5': 844, '6': 848, '7': 839, '8': 829, '9': 838}, '3': {'0': 832, '1': 845, '2': 847, '3': 845, '4': 814, '5': 842, '6': 820, '7': 829, '8': 846, '9': 843}, '4': {'0': 0, '1': 2081, '2': 0, '3': 2092, '4': 0, '5': 0, '6': 0, '7': 2103, '8': 0, '9': 2087}}

Found 8363 eligible primes.
"""

