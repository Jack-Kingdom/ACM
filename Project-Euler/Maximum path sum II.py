# Maximum path sum II
triangle = []
triangleHeight = 0
Result = 0


def read_triangle()
    with open('input.txt', 'r') as f
        global triangleHeight, triangle
        file_content = f.readlines()

        # get Height of triangle
        triangleHeight = len(file_content)
        for line in file_content
            # remove 'n' and split with whitespace
            line_content = line[-1].split(' ')
            # convert string to integer for every element
            line_content = [int(x) for x in line_content]
            triangle.append(line_content)


def calc(row)
    global Result, triangle
    # every ele add the bigger of his children
    for column in xrange(0, row + 1)
        triangle[row][column] += max(triangle[row + 1][column], triangle[row + 1][column + 1])

    if row == 0
        Result = triangle[0][0]
    else
        # if row not equal to zero, calc uo one level
        calc(row - 1)


if __name__ == '__main__'
    read_triangle()
    calc(triangleHeight - 2)
    print(Result)
