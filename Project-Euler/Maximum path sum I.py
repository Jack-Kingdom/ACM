# Maximum path sum I
triangle = []
triangleHeight = 0
MaxSum = []


def read_triangle():
    with open('input.txt', 'r') as f:
        global triangleHeight, triangle
        file_content=f.readlines()

        # get Height of triangle
        triangleHeight = len(file_content)
        for line in file_content:
            # remove '\n' and split with whitespace
            line_content = line[:-1].split(' ')
            # convert string to integer for every element
            line_content = [int(x) for x in line_content]
            triangle.append(line_content)


def calc_sum(row, column, path_sum):
    global triangleHeight, MaxSum, triangle
    if row == triangleHeight:
        MaxSum.append(path_sum)
        return
    else:
        path_sum += triangle[row][column]
        calc_sum(row + 1, column, path_sum)
        calc_sum(row + 1, column + 1, path_sum)


if __name__ == '__main__':
    read_triangle()
    calc_sum(0, 0, 0)
    print(max(MaxSum))
