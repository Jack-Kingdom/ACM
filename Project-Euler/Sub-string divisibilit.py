# Sub-string divisibility

pandigital_num_sum = 0


def get_3num(lst, start):
    out = lst[start] * 100 + lst[start + 1] * 10 + lst[start + 2]
    return out


def judge(lst):
    if get_3num(lst, 1) % 2 == 0:
        if get_3num(lst, 2) % 3 == 0:
            if get_3num(lst, 3) % 5 == 0:
                if get_3num(lst, 4) % 7 == 0:
                    if get_3num(lst, 5) % 11 == 0:
                        if get_3num(lst, 6) % 13 == 0:
                            if get_3num(lst, 7) % 17 == 0:
                                return True
    else:
        return False


def calc_sum(lst):
    if judge(lst):
        pandigital_num = 0
        # turn lst into num
        for ele in lst:
            pandigital_num *= 10
            pandigital_num += ele
        global pandigital_num_sum
        # add to sum
        pandigital_num_sum += pandigital_num


def perm(lst, seq, length):
    # seq is number's sequence of lst, length is length of lst
    if seq >= length:
        # here output
        calc_sum(lst)
    else:
        for i in xrange(seq, length):
            lst[seq], lst[i] = lst[i], lst[seq]
            perm(lst, seq + 1, length)
            lst[seq], lst[i] = lst[i], lst[seq]


if __name__ == '__main__':
    lst = range(10)
    perm(lst, 0, len(lst))
    print(pandigital_num_sum)
