# Number spiral diagonals

step_length = 2
last_num = 1
result = 0


# generate four number of a circle and return its sum
def generate_circle_sum():
    global last_num, step_length
    circle_sum = 0
    # sum equal to sum of four num
    for x in xrange(4):
        last_num += step_length
        circle_sum += last_num
    # the outer layer, step_length add 2
    step_length += 2
    return circle_sum


if __name__ == '__main__':
    # 1001 has 500 circles
    for i in xrange(500):
        result += generate_circle_sum()
    # the center, result add 1
    result += 1
    print(result)
