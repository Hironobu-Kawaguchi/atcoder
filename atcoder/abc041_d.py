# https://atcoder.jp/contests/abc041/tasks/abc041_d

# https://atcoder.jp/contests/abc041/submissions/2018700
def d_Footrace(N, M, R):
    # i番目の要素の値は、i番目のうさぎより早かったうさぎの番号を意味する
    # j番のうさぎがより早かった場合、下からj番目のビットを1にする
    # 例:x,y=2,3(x-1,y-1=1,2) -> faster[2] => 0b10(0d2)
    faster = [0] * N
    for x, y in R:
        faster[y - 1] += 1 << (x - 1)

    bit_max = 1 << N  # うさぎはN匹いるので、2^Nまで用意する
    dp = [0] * bit_max
    dp[0] = 1  # 空集合をトポロジカルソートする並べ方は1通りとする

    for bitset in range(bit_max):
        # bitsetを2進法で表したとき,下からi番目のビットが1ならi番目のうさぎがいることを表す
        for rabbit in range(N):
            rabbit_binary = 1 << rabbit  # うさぎの番号をビット列に変換
            others = bitset - rabbit_binary  # (解説におけるS-{v}の部分)
            if bitset & rabbit_binary and faster[rabbit] & others == faster[rabbit]:
                # bitsetのなかに注目しているうさぎがいる
                # かつ 「注目しているうさぎより早いうさぎの集合」が「現在の集合」に含まれている
                # そのときだけ遷移できる
                dp[bitset] += dp[bitset - rabbit_binary]
    return dp[-1]

N,M = [int(i) for i in input().split()]
R = [[int(i) for i in input().split()] for j in range(M)]
print(d_Footrace(N, M, R))
