# https://atcoder.jp/contests/abc096/tasks/abc096_b

ABC = list(map(int, input().split()))
K = int(input())

ans = max(ABC) * (2**K-1) + sum(ABC)

print(ans)
