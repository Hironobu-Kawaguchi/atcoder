# https://codingcompetitions.withgoogle.com/codejam/round/0000000000877b42/0000000000afe6a1

from string import ascii_uppercase
d = dict(zip(ascii_uppercase, range(26)))
# print(d)

def solve(x):
    N = int(input())
    S = input().split()
    # print(S)

    def all_same(s):
        s0 = s[0]
        for c in s:
            if c!=s0:
                return False
        return True

    chgS = []
    same_cnt = [0] * 26
    for s in S:
        if all_same(s):
            same_cnt[d[s[0]]] += len(s)
        else:
            chgS.append(s)
    for i in range(26):
        if same_cnt[i]!=0:
            for j, s in enumerate(chgS):
                if s[0]==ascii_uppercase[i]:
                    chgS[j] = ascii_uppercase[i]*same_cnt[i] + chgS[j]
                    break
                elif s[-1]==ascii_uppercase[i]:
                    chgS[j] += ascii_uppercase[i]*same_cnt[i]
                    break
            else:
                chgS.append(ascii_uppercase[i]*same_cnt[i])
    # print(chgS)

    flag = True
    G = [[[] for _ in range(26)] for _ in range(3)]
    for idx, s in enumerate(chgS):
        G[0][d[s[0]]].append(idx)
        G[2][d[s[-1]]].append(idx)
        ss = s[0]
        for j in range(len(s)-1):
            if s[j]!=s[j+1]:
                ss += s[j+1]
        # st = set()
        # st.add(s[0]); st.add(s[-1])
        # print(s[0])
        for j in range(1, len(ss)-1):
            if ss[0]==ss[-1]: # 最初と最後が同じで途中違うはダメ
                flag = False
                # print(ss)
                break
            G[1][d[ss[j]]].append(idx)
            # st.add(c)
    # print(G)
    for j in range(26):
        for i in range(3):
            if len(G[i][j])>=2:
                flag = False
                # print(i, j, G[i][j])
        if len(G[1][j])>0 and (len(G[0][j])>0 or len(G[2][j])>0):
            flag = False
    if flag is False:
        y = 'IMPOSSIBLE'
        print(f"Case #{x}: {y}")
        return
    y = ''
    done = [False] * len(chgS)
    for i in range(len(chgS)):
        if done[i]: continue
        now = i
        while True:
            if done[now]: break
            if chgS[now][0]==chgS[now][-1]: break
            if len(G[2][d[chgS[now][0]]])==1:
                now = G[2][d[chgS[now][0]]][0]
            else:
                break
            if now==i:
                flag = False
                y = 'IMPOSSIBLE'
                print(f"Case #{x}: {y}")
                return
        # print(now, chgS[now], done)
        while True:
            if done[now]: break
            y += chgS[now]
            done[now] = True
            # print(y, now, G[0][d[chgS[now][-1]]], done)
            if len(G[0][d[chgS[now][-1]]])==1:
                now = G[0][d[chgS[now][-1]]][0]
            else:
                break
    for i in range(len(chgS)):
        if done[i]: continue
        y += chgS[i]
    
    print(f"Case #{x}: {y}")

T = int(input())
for t in range(T):
    solve(t+1)
