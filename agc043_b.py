# https://atcoder.jp/contests/agc043/tasks/agc043_b
import sys
def input(): return sys.stdin.readline().rstrip()

N = int(input())
a = input()
# a = '1' * N

def bit_count(i):
    res = 0
    while ((i>0) and (i&1 == False)):
        i  >>=1
        res += 1
        # print(i)
    return res

f = [0]
for i in range(N//2):
    f.append(f[-1] + bit_count(N-1-i) - bit_count(i+1))

def nCr(n, r):
    if r > n-r: r = n-r
    if f[r] == 0:   # 奇数
        return 1
    else:
        return 0

def main():
    ans = 0
    for i in range(N):
        now = int(a[i]) - 1     # 全体を1引いても同じ
        if now%2:
            # print(i, nCr(N-1, i))
            ans += now * (nCr(N-1, i) % 2)
            ans %= 2
    if ans:
        return ans

    if '2' in a:    # 答えが奇数でなく、入力に2が含まれる場合は答えは0
        return 0

    ans = 0
    for i in range(N):
        now = (int(a[i]) - 1) // 2     # 全体を1引いても同じ
        if now%2:
            ans += now * (nCr(N-1, i) % 2)
            ans %= 2
    return ans*2    # 答えは0か2なので2倍して出す

print(main())
