# https://atcoder.jp/contests/arc007/tasks/arc007_2

N, M = map(int, input().split())
box = list(range(N+1))
for i in range(M):
    disk = int(input())
    for j in range(N+1):
        if box[j] == disk:
            break
    box[j] = box[0]
    box[0] = disk
for i in range(1, N+1):
    print(box[i])
