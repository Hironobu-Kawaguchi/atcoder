# http://codeforces.com/contest/1551/problem/B2

from collections import Counter

def main():
    n, k = map(int, input().split())
    # print(n, k)
    a = list(map(int, input().split()))
    cnt = Counter(a)
    # print(cnt)
    color_nums = 0
    nums_idx = []
    for i, v in cnt.items():
        color_nums += min(v, k)
        # print(color_nums, k, v)
        nums_idx.append([min(v, k), i])
    # print(color_nums)
    nums_idx.sort(reverse=True)
    # print(nums_idx)
    allocation = [[] for _ in range(k)]
    now = 0
    max_cnt = color_nums // k
    for v, i in nums_idx:
        for j in range(v):
            if len(allocation[now])==max_cnt: continue
            allocation[now].append(i)
            now += 1
            now %= k
    # print(allocation)
    nums_alloc = [[] for _ in range(n)]
    for j, idx_list in enumerate(allocation):
        for i in idx_list:
            nums_alloc[i-1].append(j+1)
    # print(nums_alloc)
    ans = []
    for i in range(n):
        if len(nums_alloc[a[i]-1]):
            ans.append(nums_alloc[a[i]-1][-1])
            nums_alloc[a[i]-1].pop()
        else:
            ans.append(0)
    print(*ans)
    return

t = int(input())
for i in range(t):
    main()
