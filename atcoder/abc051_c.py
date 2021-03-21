# A - Haiku
# https://atcoder.jp/contests/abc051/tasks/abc051_a

sx, sy, tx, ty = map(int, input().split())
ans = (   "U" * (ty - sy)     + "R" * (tx - sx) +
          "D" * (ty - sy)     + "L" * (tx - sx) +
    "L" + "U" * (ty - sy + 1) + "R" * (tx - sx + 1) + "D" +
    "R" + "D" * (ty - sy + 1) + "L" * (tx - sx + 1) + "U"
    )
print(ans)
