# Amicable numbers
Maxnum = 10000


def proper_divisor_sum(num):
    divisors = []
    for i in xrange(1, num):
        if num % i == 0:
            divisors.append(i)
    return sum(divisors)


def amicable_numbers():
    result = []
    for i in xrange(1, Maxnum):
        if i == proper_divisor_sum(proper_divisor_sum(i)) and i != proper_divisor_sum(i):
            result.append(i)
    return result


if __name__ == '__main__':
    out = amicable_numbers()
    print(out)
    print("out: " + str(sum(out)))
