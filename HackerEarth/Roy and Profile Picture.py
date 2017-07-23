L=int(input())
N=int(input())
for _ in range(N):
    W,H=map(int,input().split(" "))
    if min(W,H)>=L:
        if W==H:
            print("ACCEPTED")
        else:
            print("CROP IT")
    else:
        print("UPLOAD ANOTHER")