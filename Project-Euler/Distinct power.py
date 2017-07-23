# Distinct powers
Min = 2
Max = 100
sequence = {}


def generate_sequence():
    for a in xrange(Min, Max + 1):
        for b in xrange(Min, Max + 1):
            sequence[a ** b] = 1

if __name__=='__main__':
    generate_sequence()
    print(len(sequence))