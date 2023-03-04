# https://atcoder.jp/contests/abc291/tasks/abc291_e
# トポロジカルソート

import sys
input = sys.stdin.buffer.readline

def main():
    N, M = map(int, input().split())
    to = [[] for _ in range(N)]
    indeg = [0]*N
    for i in range(M):
        x, y = map(int, input().split())
        to[x-1].append(y-1)
        indeg[y-1] += 1
    q = []
    for i in range(N):
        if indeg[i]==0:
            q.append(i)
    A = [-1]*N
    now = 1
    while q:
        if len(q)>1:
            print("No")
            return
        x = q.pop()
        A[x] = now
        now += 1
        for y in to[x]:
            indeg[y] -= 1
            if indeg[y]==0:
                q.append(y)
    print("Yes")
    print(*A)
    return

main()



# import sys
# input = sys.stdin.buffer.readline
# def main():
#     N, M = map(int, input().split())
#     to = [set() for _ in range(N)]
#     frm = [set() for _ in range(N)]
#     for i in range(M):
#         x, y = map(int, input().split())
#         to[x-1].add(y-1)
#         frm[y-1].add(x-1)
#     start, end = [], []
#     for i in range(N):
#         if len(to[i])==0:
#             end.append(i)
#         if len(frm[i])==0:
#             start.append(i)
#     if len(start)!=1 or len(end)!=1:
#         print("No")
#         return
    
#     now = start[0]
#     q = [now]
#     route = []
#     err = False
#     while q:
#         now =  q.pop()
#         route.append(now)
#         cnt = 0
#         for v in to[now]:
#             frm[v].remove(now)
#             if len(frm[v])==0:
#                 q.append(v)
#                 cnt += 1
#         if cnt>1:
#             # print("err", cnt, q, now)
#             err = True
#     if err:
#         print("No")
#         return
#     ans = [-1]*N
#     for i in range(N):
#         ans[route[i]] = i+1
#     print("Yes")
#     print(*ans)
    
# main()



# import sys
# input = sys.stdin.buffer.readline

# def main():
#     N, M = map(int, input().split())
#     to = [[] for _ in range(N)]
#     frm = [[] for _ in range(N)]
#     for i in range(M):
#         x, y = map(int, input().split())
#         to[x-1].append(y-1)
#         frm[y-1].append(x-1)
#     start, end = [], []
#     for i in range(N):
#         if len(to[i])==0:
#             end.append(i)
#         if len(frm[i])==0:
#             start.append(i)
#     if len(start)!=1 or len(end)!=1:
#         print("No")
#         return

#     dp = [set() for _ in range(N)]
#     dp[0].add(end[0])
#     for i in range(N-1):
#         for u in dp[i]:
#             for v in frm[u]:
#                 dp[i+1].add(v)
#     # print(dp)
#     if len(dp[N-1])!=1:
#         print("No")
#         return
#     route = []
#     for i in range(N-1, -1, -1):
#         if len(dp[i])==1:
#             route.append(list(dp[i])[0])
#         else:
#             for u in to[route[-1]]:
#                 if u in dp[i]:
#                     route.append(u)
#                     break
#     # print(ans)
#     if len(route)!=N or route[-1]!=end[0]:
#         print("No")
#         return
#     print("Yes")
#     ans = [-1]*N
#     for i in range(N):
#         ans[route[i]] = i+1
#     print(*ans)
#     return

# main()


# TLE
# import sys
# input = sys.stdin.buffer.readline
# # def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

# def main():
#     N, M = map(int, input().split())
#     to = [[] for _ in range(N)]
#     frm = [[] for _ in range(N)]
#     for i in range(M):
#         x, y = map(int, input().split())
#         to[x-1].append(y-1)
#         frm[y-1].append(x-1)
#     # print(to)
#     # print(frm)

#     start, end = [], []
#     for i in range(N):
#         if len(to[i])==0:
#             end.append(i)
#         if len(frm[i])==0:
#             start.append(i)
#     # print(start)
#     # print(end)
#     if len(start)!=1 or len(end)!=1:
#         print("No")
#         return
#     dist = [-1]*N
#     dist[end[0]] = 0
#     flg = [True]

#     def dfs(u, d):
#         if flg[0]==False:
#             # print("Chek")
#             return
#         if d>N+1:
#             flg[0] = False
#             return
#         if dist[u]<d:
#             dist[u] = d
#         for v in frm[u]:
#             dfs(v, d+1)
#         return

#     dfs(end[0], 0)
#     # print(flg)
#     # print(dist)
#     if flg[0]==False:
#         print("No")
#         return
#     ans = [-1]*N
#     for i in range(N):
#         if dist[N-1-i]==-1 or dist[N-1-i]>=N or ans[dist[N-1-i]]!=-1:
#             print("No")
#             return
#         ans[dist[N-1-i]] = i+1
#     print("Yes")
#     print(*ans)
#     return

# main()

