# https://atcoder.jp/contests/chokudai004/tasks/chokudai004_a
import sys
input = sys.stdin.buffer.readline
import numpy as np

N, B1, B2, B3 = map(int, input().split())
l = np.array([[int(i) for i in input().split()] for _ in range(N)], dtype=np.int32)
r = np.array([[int(i) for i in input().split()] for _ in range(N)], dtype=np.int32)

def calc_point(arr):
    ret = 0
    for i in range(N-1):
        for j in range(i+1, N):
            for k in range(N):
                sm = sum(arr[k, i:j])
                if sm == B1:
                    ret += B1
                elif sm == B2:
                    ret += B2
                elif sm == B3:
                    ret += B3
                sm = sum(arr[i:j, k])
                if sm == B1:
                    ret += B1
                elif sm == B2:
                    ret += B2
                elif sm == B3:
                    ret += B3
    return ret

ans = r
ans_point = calc_point(ans)
for i in range(10):
    dif = np.random.randint(0, 8, (N, N), dtype=np.int32)
    candidate = np.clip(l + dif, l, r)
    can_point = calc_point(candidate)
    if can_point > ans_point:
        ans = candidate
        ans_point = can_point

for i in range(N):
    print(*ans[i])
# print(ans_point)
