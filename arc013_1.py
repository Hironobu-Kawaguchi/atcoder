# https://atcoder.jp/contests/arc013/tasks/arc013_1

from itertools import permutations
NML = list(map(int, input().split()))
PQR = list(map(int, input().split()))

ans = 0
for i, j, k in permutations(range(3)):
    # print(i, j, k)
    ans = max(ans, (NML[0]//PQR[i]) * (NML[1]//PQR[j]) * (NML[2]//PQR[k]))

print(ans)
