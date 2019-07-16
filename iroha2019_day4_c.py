# C - 君の力に
# https://atcoder.jp/contests/iroha2019-day4/tasks/iroha2019_day4_c

def magic(s):
    s_ = s[:2]
    for i in range(2, len(s)):
        if s[i - 2] == s[i]:
            s_ += "0"
        else:
            s_ += "1"
    return s_

def search(S, m, M):
    t, m_ = 0, 0
    while True:
        if S > m[m_][1]:
            m_ += 1
        else:
            if S[:2] < m[m_][1][:2]:
                print("No")
                return
            S = magic(S)
            t += 1
            c = 0
            while S <= m[m_][1]:
                S = magic(S)
                t += 1
                c += 1
                if c == 10:
                    print("No")
                    return
            if t > m[m_][0]:
                print("No")
                return
            m_ += 1
        if m_ == M:
            print("Yes")
            return

S = input()
M = int(input())
m = []

for _ in range(M):
    tmp = input().split()
    m.append([int(tmp[0]), tmp[1]])
m.sort()

search(S, m, M)

"""
S = input()
M = int(input())
x = []
s = []
ls = []
chk = [0] * M
for i in range(M):
    _x, _s = input().split()
    if S[:2] < _s[:2]:
        print('No')
        exit()
    elif S[:2] > _s[:3]:
        chk[i] = 1
    x.append(int(_x))
    s.append(_s)
    ls.append(len(_s))

if all(chk):
    print('Yes')
    exit()

maxs = S
ans = S
cnt = 0
mcnt = 0
# for i in range(x[-1]):
for i in range(min(x[-1], 255)):
    tmp = ans[:2]
    for j in range(len(ans)-2):
        if ans[j] == ans[j+2]:
            tmp += '0'
        else:
            tmp += '1'
    maxs = max(ans, maxs)
    ans = tmp
    cnt += 1
    # print(ans, maxs, cnt)
    if x[mcnt] == cnt:
        if maxs <= s[mcnt]:
            # print('Lose', maxs, s[cnt-1])
            print('No')
            exit()
        mcnt += 1

if mcnt < M:
    for i in range(mcnt, M):
        if maxs <= s[i]:
            print('No')
            exit()

print('Yes')
"""

"""
111111111111111111111111111111111111111111111111111111111111111
1
256 110111111111111111111111111111111111111111111111111111111111111
"""
