# Lexicographic permutations

import itertools

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sequence = itertools.permutations(digits)

No = 1000000
for x in xrange(No-1):
    sequence.next()
print(sequence.next())