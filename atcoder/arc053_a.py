# https://atcoder.jp/contests/arc053/tasks/arc053_a

H, W = map(int, input().split())
ans = (H-1)*W + H*(W-1)
print(ans)
