S = input()

RS = list(S)
RS.reverse()
RS = "".join(RS)

if S == RS:
    print("YES")
else:
    print("NO")