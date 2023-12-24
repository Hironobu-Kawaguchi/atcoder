# https://atcoder.jp/contests/abc328/tasks/abc328_b

# import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N = int(input())
D = list(map(int, input().split()))

def check(m, d):
    s = str(m) + str(d)
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            return False
    return True

ans = 0
for m in range(1, N+1):
    for d in range(1, D[m-1]+1):
        if check(m, d):
            ans += 1
            # print(m, d)
print(ans)
