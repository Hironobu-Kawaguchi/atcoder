# https://atcoder.jp/contests/abc139/tasks/abc139_b
import math
A, B = map(int, input().split())
ans = math.ceil((B-1) / (A-1))
print(ans)
