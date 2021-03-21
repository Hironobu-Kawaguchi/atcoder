# https://atcoder.jp/contests/abc172/tasks/abc172_d

n = int(input())
ans = 0
for i in range(1,n+1):
    tmp = n//i
    ans += (tmp*(tmp+1)//2)*i
print(ans)

# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
