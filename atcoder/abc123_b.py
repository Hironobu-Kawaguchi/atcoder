# B - Five Dishes
# https://atcoder.jp/contests/abc123/tasks/abc123_b
"""
A = [int(input()) for i in range(5)]
B = [a - a % 10 + 10 if a % 10 != 0 else a for a in A]
diff = [(b - a) for a, b in zip(A, B)]

print(sum(B)-max(diff))
"""
l = [int(input()) for _ in range(5)]
mod = 10
sm = 0
for i in l:
    if i % 10 != 0:
        mod = min(mod, i % 10)
    sm += -10*(-i//10)
if mod == 10:
    mod = 0
else:
    sm -= 10
print(mod+sm)