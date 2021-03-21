# I - Prime or Not
# https://atcoder.jp/contests/iroha2019-day3/tasks/iroha2019_day3_i

A = 9 * 10 ** 15 + 1
B = A + 2018
# B = 10 ** 16 -1
# A = B - 2018
print(A, B)

"""
sosuset = set([2])
for i in range(3, 9*10**4):
    flg = True
    for j in sosuset:
        if i % j == 0:
            flg = False
            break
    if flg:
        sosuset.add(i)

print(sosuset)
"""