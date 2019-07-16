"""
C - Synthetic Kadomatsu
https://atcoder.jp/contests/abc119/tasks/abc119_c
あなたは N 本の竹を持っています。これらの長さはそれぞれ l1,l2,...,lN です (単位: センチメートル)。
あなたの目的は、これらの竹のうち何本か (全部でもよい) を使い、長さが A,B,C であるような 3 本の竹を得ることです。
そのために、以下の三種類の魔法を任意の順に何度でも使うことができます。
- 延長魔法: 1 MP (マジックポイント) を消費し、1 本の竹を選んでその長さを 1 増やす。
- 短縮魔法: 1 MP を消費し、1 本の長さ 2 以上の竹を選んでその長さを 1 減らす。
- 合成魔法: 10 MP を消費し、2 本の竹を選んで接続し 1 本の竹とする。この新たな竹の長さは接続した 2 本の竹の長さの合計に等しい。(以後、この竹に対してさらに魔法を使用することもできる。)
目的を達成するには、最小でいくつの MP が必要でしょうか？
"""
"""
N, A, B, C = map(int, input().split())
l = [int(input()) for i in range(N)]
INF = 10 ** 9
def dfs(cur, a, b, c):
    if cur == N:
        return abs(a - A) + abs(b - B) + abs(c - C) - 30 if min(a, b, c) > 0 else INF
    ret0 = dfs(cur + 1, a, b, c)
    ret1 = dfs(cur + 1, a + l[cur], b, c) + 10
    ret2 = dfs(cur + 1, a, b + l[cur], c) + 10
    ret3 = dfs(cur + 1, a, b, c + l[cur]) + 10
    return min(ret0, ret1, ret2, ret3)
print(dfs(0, 0, 0, 0))
"""
N, A, B, C = map(int, input().split())
l = [int(input()) for _ in range(N)]
def dfs(cur, a, b, c):
    if cur == N:
        return abs(a-A) + abs(b-B) + abs(c-C) - 30 if a * b * c != 0 else 10 ** 9
    else:
        ret0 = dfs(cur + 1, a, b, c)
        reta = dfs(cur + 1, a + l[cur], b, c) + 10
        retb = dfs(cur + 1, a, b + l[cur], c) + 10
        retc = dfs(cur + 1, a, b, c + l[cur]) + 10
        return min(ret0, reta, retb, retc)
print(dfs(0,0,0,0))
