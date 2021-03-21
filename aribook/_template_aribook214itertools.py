# 蟻本をPythonで (初級編)
# https://qiita.com/saba/items/affc94740aff117d2ca9
# 例題 2-1-4　特殊な状態の列挙
# Python には順列や組み合わせを列挙することのできる itertools というライブラリがあります。

import itertools

# 順列
# permutations(list, n) で list から n 個選んで並べる
for i in itertools.permutations([0, 1, 2], 3):
    print(i)
# (0, 1, 2)
# (0, 2, 1)
# (1, 0, 2)
# (1, 2, 0)
# (2, 0, 1)
# (2, 1, 0)


# 組み合わせ
# combinations(list, n) で list から n 個選ぶ
for i in itertools.combinations([0, 1, 2], 2):
    print(i)
# (0, 1)
# (0, 2)
# (1, 2)