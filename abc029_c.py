# C - Brute-force Attack
# https://abc029.contest.atcoder.jp/tasks/abc029_c

N = int(input())
strs = ['a', 'b', 'c']

def dfs(n, temp):
    if n == N:
        print(temp)
    else:
        for x in strs:
            dfs(n+1, temp + x)

dfs(0, '')
