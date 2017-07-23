S = input()
result = ''
for alpha in S:
    if alpha.isupper():
        result += alpha.lower()
    else:
        result += alpha.upper()

print(result)
