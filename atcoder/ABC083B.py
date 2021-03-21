# B - Some Sums
# https://atcoder.jp/contests/abc083/tasks/abc083_b
# 1  以上 N 以下の整数のうち、10 進法での各桁の和が A 以上 B 以下であるものの総和を求めてください。

N ,A, B = map(int, input().split())
num = 0
for i in range(1, N+1):
    nsum = sum(map(int, str(i)))
    if A <= nsum and nsum <= B:
        num += i
print(num)
