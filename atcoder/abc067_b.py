# https://atcoder.jp/contests/abc067/tasks/abc067_b

N, K = map(int, input().split())
l = list(map(int, input().split()))
l.sort(reverse=True)

ans = sum(l[:K])
print(ans)