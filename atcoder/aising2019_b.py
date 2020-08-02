# https://atcoder.jp/contests/aising2019/tasks/aising2019_b

N = int(input())
A, B = map(int, input().split())
P = list(map(int, input().split()))

cnt = [0] * 3
for i in range(N):
    if P[i] <= A:
        cnt[0] += 1
    elif P[i] <= B:
        cnt[1] += 1
    else:
        cnt[2] += 1
print(min(cnt))
