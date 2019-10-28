# https://atcoder.jp/contests/abc144/tasks/abc144_e

N, K = map(int, input().split())
A = list(map(int, input().split()))
F = list(map(int, input().split()))
A.sort()
F.sort(reverse=True)

start = -1
end = A[-1] * F[0]

def check(now):
    cnt = 0
    for a, f in zip(A, F):
        eatable = now//f
        if eatable < a:
            cnt += a - eatable
    if cnt > K:
        return False
    return True

while end > start + 1:
    now = (start + end) // 2
    if check(now):
        end = now
    else:
        start = now

print(end)
