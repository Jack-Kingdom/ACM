N = int(input())
array = list(map(int, input().split(' ')))

result = 1
for i in array:
    result = (result * i) % (10 ** 9 + 7)

print(result)
