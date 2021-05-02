# https://codeforces.com/contest/1515/problem/B

import heapq

def main():
    n, m, x = map(int, input().split())
    h = list(map(int, input().split()))
    h = list(zip(h, range(n)))
    h.sort(reverse=True)
    # print(h)
    ans = [0]*n
    q = []
    max_sum = 0
    for i in range(m):
        heapq.heappush(q, (h[i][0], i+1))
        ans[h[i][1]] = i+1
        max_sum = max(max_sum, h[i][0])
    for i in range(m, n):
        sumh, mi = heapq.heappop(q)
        heapq.heappush(q, (sumh + h[i][0], mi))
        ans[h[i][1]] = mi
        max_sum = max(max_sum, sumh + h[i][0])
    # print(ans)
    # print(q)
    # print(max_sum)
    if max_sum - q[0][0] > x:
        print("NO")
    else:
        print("YES")
        print(*ans)
    return

t = int(input())
for _ in range(t):
    main()
