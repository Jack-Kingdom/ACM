# Names scores

Names = []
alphabet_value = {}


def read_names():
    global Names
    with open('input.txt', 'r') as f:
        # delete quotation and split by ','
        Names = f.readline().replace('"', '').split(',')
        # sort by dictionary
        Names.sort()


def generate_alphabet_value():
    global alphabet_value
    alphabet_table = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    for i in xrange(len(alphabet_table)):
        alphabet_value[alphabet_table[i]] = i + 1


def calc_names_scores():
    global Names, alphabet_value
    total = 0
    for name_i in xrange(len(Names)):
        score = 0
        for char in list(Names[name_i]):
            score += alphabet_value[char]
        # name score equal to sum of alphabet value multiply position
        score *= name_i + 1
        total += score
    return total


if __name__ == '__main__':
    read_names()
    generate_alphabet_value()
    print(calc_names_scores())
