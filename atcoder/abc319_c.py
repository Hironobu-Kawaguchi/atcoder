# https://atcoder.jp/contests/abc319/tasks/abc319_c

from itertools import permutations

c = [list(map(int, input().split())) for _ in range(3)]
# print(c)
chk = [[0, 1, 2],
       [3, 4, 5],
       [6, 7, 8],
       [0, 3, 6],
       [1, 4, 7],
       [2, 5, 8],
       [0, 4, 8],
       [2, 4, 6]
]

ok, cnt = 0, 0
for p in permutations(range(9)):
    done = [False] * 9
    cnt += 1
    flg = True
    for x in p:
        done[x] = True
        for cc in chk:
            done_cnt = 0
            ns = []
            for y in cc:
                i, j = divmod(y, 3)
                if done[y]: 
                    # print(i, j, c[i][j])
                    done_cnt += 1
                    ns.append(c[i][j])
            if done_cnt == 2 and ns[0] == ns[1]:
                flg = False
                break
        if not flg:
            break
    if flg:
        ok += 1
print(ok/cnt)
# print(ok, cnt)
