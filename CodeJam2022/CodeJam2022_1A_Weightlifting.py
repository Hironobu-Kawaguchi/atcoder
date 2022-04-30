# https://codingcompetitions.withgoogle.com/codejam/round/0000000000877ba5/0000000000aa9280

# from collections import Counter
INF = 100

t = int(input())
for ti in range(1, t + 1):
    e, w = map(int, input().split())
    x = [[int(i) for i in input().split()] for _ in range(e)]

    def get_cnt(lst):
        ret = [0]*w
        for x in lst:
            ret[x] += 1
        return ret

    min_x = [INF]*w
    for i in range(e):
        for j in range(w):
            min_x[j] = min(min_x[j], x[i][j])
    for i in range(e):
        for j in range(w):
            x[i][j] -= min_x[j]
    flag = False
    ans = sum(min_x) * 2
    st = [(0, list())]
    while True:
        st_next = list()
        if len(st)==0: break
        # print(ans, flag, x[-1], st)
        for i, lst in st:
            cnt = get_cnt(lst)
            # print(cnt, x[0], i, e)
            if cnt==x[i]:
                i += 1
                if i==e:
                    flag = True
                    ans += sum(cnt)
                    break
            for j in range(w):
                if cnt[j]>=x[i][j]: continue
                st_next.append((i, lst + [j]))
            if lst:
                lst.pop()
                st_next.append((i, lst))
        if flag:
            break
        else:
            ans += 1
            st = st_next
    print("Case #{}: {}".format(ti, ans))
