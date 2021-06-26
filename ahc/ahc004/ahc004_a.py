# https://atcoder.jp/contests/ahc004/tasks/ahc004_a

from collections import defaultdict

N, M = map(int, input().split())
d = defaultdict(int)
for i in range(M):
    S = input()
    d[S] += 1
# lst = sorted(d.items(), key=lambda x:x[1], reverse=True)
# lst = [k for k, v in lst]
lst = sorted(d.keys(), key=lambda x: len(x), reverse=True)
# print(len(lst), lst)

for i in range(len(lst)-1):
    for j in range(i+1, len(lst)):
        if lst[j] in lst[i]:
            if lst[j] in d:
                d[lst[i]] += d[lst[j]]
                d.pop(lst[j])
            break
# print(len(d), sorted(d.items(), key=lambda x:x[1], reverse=True))

for k in range(1,5):
    for j in range(5):
        lst = sorted(d.items(), key=lambda x:x[1], reverse=True)
        lst = [k for k, v in lst]
        for i in range(len(lst)):
            # if len(lst[i])+k>20: continue
            if len(lst[i])<=k+5-j: continue
            for st, v in sorted(d.items(), key=lambda x:x[1], reverse=True):
                if len(st)+k>20: continue
                if lst[i]==st: continue
                if d[lst[i]] + d[st] <= k+2: continue
                if st in lst[i]:
                    d[lst[i]] += d[st]
                    del d[st]
                    # if d[lst[i]]==0:
                    #     print(lst[i], d[lst[i]])
                    break
                l = len(lst[i])
                if len(st)<l: continue
                if lst[i][k:]==st[:l-k]:
                    newst = lst[i][:k] + st
                    if lst[i] not in d: continue
                    if st not in d: continue
                    d[newst] += d[lst[i]] + d[st]
                    # if d[newst]==0:
                    #     print(newst, d[newst])
                    del d[lst[i]]
                    # if lst[i] in d:
                    #     print(lst[i], d[lst[i]])
                    del d[st]
                    # if st in d:
                    #     print(st, d[st])
                    break
                if lst[i][:l-k]==st[-l+k:]:
                    newst = st + lst[i][-k:]
                    if lst[i] not in d: continue
                    if st not in d: continue
                    d[newst] += d[lst[i]] + d[st]
                    # if d[newst]==0:
                    #     print(newst, d[newst])
                    del d[lst[i]]
                    # if lst[i] in d:
                    #     print(lst[i], d[lst[i]])
                    del d[st]
                    # if st in d:
                    #     print(st, d[st])
                    break
        # print(len(s))
# print(len(d), sorted(d.items(), key=lambda x:x[1], reverse=True))

best_ans = [['.']*N for _ in range(N)]
best_point = 0
lst = sorted(d.items(), key=lambda x:x[1], reverse=True)
# print(len(lst), lst)
for idx in range(10):
    ans = [['.']*N for _ in range(N)]
    used = [0]*N
    start = [0]*N
    point = d[lst[idx][1]]
    for i, c in enumerate(lst[idx][0]):
        ans[i][0] = c
        used[i] = 1
    rest = []
    for x, (st, v) in enumerate(lst):
        if v==0: continue
        if x==idx: continue
        for i in range(N):
            if used[i]==0 and ans[i][0] in st:
                j = st.find(ans[i][0])
                for k, c in enumerate(st):
                    ans[i][(used[i]+k+N-j)%N] = c
                used[i] += len(st)
                start[i] = (N-j)%N
                point += v
                break
            if N-used[i]>=len(st):
                for k, c in enumerate(st):
                    ans[i][(used[i]+k+start[i])%N] = c
                used[i] += len(st)
                point += v
                break
        else:
            rest.append((st, v))
            continue
    if point > best_point:
        best_ans = ans
    # print(len(rest), rest)

# print(best_ans)
for i in range(N):
    print(''.join(best_ans[i]))
