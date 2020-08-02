# D - カード並べ
# https://atcoder.jp/contests/joi2010yo/tasks/joi2010yo_d

import itertools

n = int(input())
k = int(input())
card = [input() for i in range(n)]

# set を使うと重複せずに数えられる
number = set()
# card から k 個選んで並び替える
for i in itertools.permutations(card, k):
    # 並び替えたものを繋げて1つの文字列にする
    number.add("".join(i))

print(len(number))