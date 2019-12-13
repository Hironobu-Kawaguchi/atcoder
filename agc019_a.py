# https://atcoder.jp/contests/agc019/tasks/agc019_a

Q, H, S, D = map(int, input().split())
N = int(input())

p1 = min(Q*4, min(H*2, S))
p2 = min(p1*2, D)

ans = N//2 * p2 + N%2 * p1
print(ans)
