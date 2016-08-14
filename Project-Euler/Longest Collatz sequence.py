# Longest Collatz sequence

RecordLength = 1000000

# CollatzLength is a list record digit's Collatz Length
# give a init value
CollatzLength = {1: 1}


def LenCollatz(num):
    # if CollatzLength not contain this digit, add one
    if num not in CollatzLength:
        CollatzLength[num] = 0

    if CollatzLength[num] != 0:
        return CollatzLength[num]
    else:
        # CollatzLength[num]==0
        if num % 2 == 1:
            child_length = LenCollatz(3 * num + 1)
        else:
            child_length = LenCollatz(num / 2)
        CollatzLength[num] = child_length + 1
        return CollatzLength[num]


if __name__ == '__main__':
    MaxLength = 0
    StartNum = 0
    for x in xrange(1, RecordLength):
        tmp = LenCollatz(x)
        # save MaxLength
        if tmp > MaxLength:
            StartNum = x
            MaxLength = tmp
    print(str(StartNum) + ' : ' + str(MaxLength))
