# B - AtCoder Beginner Contest 111
# https://atcoder.jp/contests/abc111/tasks/abc111_b

N = input()
tmp = N[0] * 3
if N > tmp:
    tmp = str(int(N[0])+1) * 3
print(tmp)
