# https://atcoder.jp/contests/abc162/tasks/abc162_b

N = int(input())
ans = 0
for i in range(1,N+1):
    if i%3 and i%5:
        ans += i
print(ans)


# S = input()
# X, Y, Z = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
