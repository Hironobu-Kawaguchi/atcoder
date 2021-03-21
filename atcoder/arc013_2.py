# https://atcoder.jp/contests/arc013/tasks/arc013_2

C = int(input())
maxsize = [0] * 3
for i in range(C):
    size = list(map(int, input().split()))
    size.sort()
    for j in range(3):
        maxsize[j] = max(maxsize[j], size[j])
ans = 1
for j in range(3):
    ans *= maxsize[j]
print(ans)
