# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd74/00000000002b1353

# 2**30 = 1073741824 > 10**9 なので、Nは30桁の2進数で表記でき、30行で足りる。ただし、各行1は加算されるので、30を引く。
# 30*(31)/2 = 465 で　500以内に収まる

def solve(N):
    if N <= 500:    # 30未満の場合の対応 500までは1*500でいける
        for i in range(1, N + 1):
            yield (i, 1)
        return
    M = N - 30
    take_row = [0] * 30
    for i in range(30):
        if M & (1 << i):
            take_row[i] = 1     # 1の行は全て使用、0の行は隅の1だけ使用し、次の行へ
    n_row = 30 + sum(take_row)  # 全て使用する行の分、31行目から隅の1だけ使用する
    from_left = True
    for r in range(n_row):
        if r >= 30 or (not take_row[r]):
            k = 1 if from_left else r + 1
            yield (r + 1, k)    # 隅の1だけ使用
            continue
        rng = range(1, r + 2) if from_left else range(r + 1, 0, -1)
        for k in rng:   # 行の全てを使用
            yield (r + 1, k)
        from_left = not from_left   # 全て使用する行は交互に移動

T = int(input())
for i in range(T):
    N = int(input())
    print('Case #{}:'.format(i+1))
    for a, b in solve(N):
        print(a, b)
