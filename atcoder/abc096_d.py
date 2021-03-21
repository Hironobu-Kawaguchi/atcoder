# https://atcoder.jp/contests/abc096/tasks/abc096_d

N = int(input())

def isprime(p):
    if p == 1:
        return False
    for i in range(2, int(p**0.5+1)):
        if p%i == 0:
            return False
    return True

ans = []
for i in range(11, 55556, 10):
    if isprime(i):
        ans.append(i)
        N -= 1
    if N == 0:
        break
print(*ans)
