# https://atcoder.jp/contests/genocon2021/tasks/genocon2021_c

INF = 1001001001

def pairwise_alignment(s, t, s_add=True):
    dp = [[-INF] * (len(t)+1) for _ in range(len(s)+1)]
    dp[0][0] = 0
    # print(dp)
    # dps = [[''] * (len(t)+1) for _ in range(len(s)+1)]
    # dpt = [[''] * (len(t)+1) for _ in range(len(s)+1)]
    # print(dps)
    frm = [[0] * (len(t)+1) for _ in range(len(s)+1)]

    for i in range(len(s)+1):
        for j in range(len(t)+1):
            if i!=0:
                if dp[i][j] < dp[i-1][j] - 1:
                    dp[i][j] = dp[i-1][j] - 1
                    frm[i][j] = 0
                    # dps[i][j] = dps[i-1][j] + s[i-1]
                    # dpt[i][j] = dpt[i-1][j] + '-'
            if j!=0 and s_add:
                if dp[i][j] < dp[i][j-1] - 1:
                    dp[i][j] = dp[i][j-1] - 1
                    frm[i][j] = 1
                    # dps[i][j] = dps[i][j-1] + '-'
                    # dpt[i][j] = dpt[i][j-1] + t[j-1]
            if i!=0 and j!=0:
                if s[i-1]==t[j-1]:
                    if dp[i][j] < dp[i-1][j-1]:
                        dp[i][j] = dp[i-1][j-1]
                        frm[i][j] = 2
                        # dps[i][j] = dps[i-1][j-1] + s[i-1]
                        # dpt[i][j] = dpt[i-1][j-1] + t[j-1]
                else:
                    if dp[i][j] < dp[i-1][j-1] - 1:
                        dp[i][j] = dp[i-1][j-1] - 1
                        frm[i][j] = 2
                        # dps[i][j] = dps[i-1][j-1] + s[i-1]
                        # dpt[i][j] = dpt[i-1][j-1] + t[j-1]

    ress, rest = '', ''
    i, j = len(s), len(t)
    while i>0 or j>0:
        if frm[i][j]==2:
            ress += s[i-1]
            rest += t[j-1]
            i -= 1
            j -= 1
        elif frm[i][j]==0:
            ress += s[i-1]
            rest += '-'
            i -= 1
        else:
            ress += '-'
            rest += t[j-1]
            j -= 1
    ress = ress[::-1]
    rest = rest[::-1]
    return ress, rest

m = int(input())
s_list = []
for i in range(m):
    s = input()
    s_list.append(s)
for i in range(1, m):
    s_list[0], s_list[i] = pairwise_alignment(s_list[0], s_list[i], s_add=True)
# for i in range(1, m, 2):
#     s_list[i-1], s_list[i] = pairwise_alignment(s_list[i-1], s_list[i], s_add=True)
# s_list.sort(reverse=True, key=len)
for i in range(1, m):
    s_list[0], s_list[i] = pairwise_alignment(s_list[0], s_list[i], s_add=False)
for i in range(m):
    print(s_list[i])

