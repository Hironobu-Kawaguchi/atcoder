# https://atcoder.jp/contests/abc039/tasks/abc039_c

S = input()
d = {"WBWBWWBWBWBW": "Do",
     "WBWWBWBWBWWB": "Re",
     "WWBWBWBWWBWB": "Mi",
     "WBWBWBWWBWBW": "Fa",
     "WBWBWWBWBWWB": "So",
     "WBWWBWBWWBWB": "La",
     "WWBWBWWBWBWB": "Si"
     }

ans = d[S[:12]]
print(ans)
