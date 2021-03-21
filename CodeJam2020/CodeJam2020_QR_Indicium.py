# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/0000000000209aa0

from itertools import permutations, product
import copy
import sys
sys.setrecursionlimit(10**7)

def main(x):
    N, K = map(int, input().split())
    K -= N
    dic_y = {0: "IMPOSSIBLE", 1: "POSSIBLE"}
    y = 0

    trace = []
    def make_trace(lst):
        tmp_sum = K - sum(lst)
        tmp_num = N - len(lst)
        if tmp_num == 0:
            if tmp_sum == 0:
                trace.append(lst)
            return
        if tmp_sum < 0:
            return
        if lst:
            max_n = lst[-1]
        else:
            max_n = 0
        for i in range(max_n, min(N, tmp_sum//tmp_num+1)):
            make_trace(lst + [i])
        return
    make_trace([])
    # print(trace)

    ans = []
    def make_latin(rat, n):
        if n == N:
            y = 1
            # print(y, rat)
            res = copy.deepcopy(rat)
            ans.append(res)
            return 1
        for p in permutations(range(N-1)):
            for c in range(N-1):
                if p[c] == rat[n][n]:
                    tmp = N-1
                else:
                    tmp = p[c]
                if c < n:
                    rat[n][c] = tmp
                else:
                    rat[n][c+1] = tmp
            chk = True
            for c in range(N):
                for r in range(n):
                    if rat[n][c] == rat[r][c]:
                        chk = False
            if chk:
                make_latin(rat, n+1)
        # return 0

    for tr in trace:
        rat = [[0]*N for _ in range(N)]
        for r in range(N):
            rat[r][r] = tr[r]
        make_latin(rat, 0)
        if ans:
            y = 1
            break
    # print(ans)
    print("Case #{}: {}".format(x, dic_y[y]))
    if y:
        for i in range(N):
            for j in range(N):
                ans[0][i][j] += 1
        for i in range(N):
            print(*ans[0][i])

T = int(input())
for i in range(T):
    main(i+1)



# from itertools import permutations
# def main(x):
#     N, K = map(int, input().split())
#     K -= N
#     rat = []
#     for r in range(N):
#         for c in range(N):
#             s = (r+c)%N
#             rat.append((r,c,s))
#     # print(rat)

#     dic_y = {0: "IMPOSSIBLE", 1: "POSSIBLE"}
#     y = 0
#     for d in permutations(range(3)):
#         for p in permutations(range(N)):
#             for q in permutations(range(N)):
#                 sumd = 0
#                 for ra in rat:
#                     if ra[d[0]] == q[ra[d[1]]]:
#                         sumd += p[ra[d[2]]]
#                 if sumd == K:
#                     y = 1
#                     break
#             if y == 1:
#                 break
#         if y == 1:
#             break

#     print("Case #{}: {}".format(x, dic_y[y]))
#     if y:
#         ans = [[0]*N for _ in range(N)]
#         for ra in rat:
#             ans[ra[d[0]]][q[ra[d[1]]]] = p[ra[d[2]]]+1
#         for i in range(N):
#             print(*ans[i])

# T = int(input())
# for i in range(T):
#     main(i+1)
