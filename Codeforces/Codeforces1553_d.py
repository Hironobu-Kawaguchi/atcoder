# http://codeforces.com/contest/1553/problem/D

def main():
    s = list(input().rstrip())
    t = list(input().rstrip())
    n = len(s)
    m = len(t)
    if n<m: return False
    p = (n-m)%2
    q, k = 0, 0
    for i in range(p, n):
        if k==1:
            k = 0
            continue
        if q<m and s[i]==t[q]:
            q += 1
        else:
            k = 1
    return q==m

q = int(input())
for i in range(q):
    if main():
        print("YES")
    else:
        print("NO")




# TLE
# from queue import Queue

# def main():
#     s = list(input().rstrip())
#     t = list(input().rstrip())
#     # print(s)
#     # print(t)
#     ans = "NO"
#     if len(s)<len(t):
#         print(ans)
#         return

#     q = Queue()
#     q.put([len(s)-1, len(t)-1])
#     while not q.empty():
#         si, ti = q.get()
#         # print(si, ti)
#         if ti<0:
#             ans = "YES"
#             break
#         if si<ti: continue
#         if s[si]==t[ti]:
#             q.put([si-1, ti-1])
#         if si>=2:
#             q.put([si-2, ti])
#     print(ans)
#     return


# q = int(input())
# for i in range(q):
#     main()


# Memory limit exceeded
# import sys
# sys.setrecursionlimit(10 ** 7)

# def main():
#     s = list(input().rstrip())
#     t = list(input().rstrip())
#     # print(s)
#     # print(t)
#     ans = ["NO"]
#     if len(s)<len(t):
#         print(ans[0])
#         return

#     def dfs(si, ti):
#         print(si, ti, ans[0])
#         if ans[0]=="YES": return
#         if ti<0:
#             ans[0] = "YES"
#             # print(si, ti, ans[0])
#             return
#         if si<ti: return
#         if s[si]==t[ti]:
#             dfs(si-1, ti-1)
#         dfs(si-2, ti)
#         return

#     dfs(len(s)-1, len(t)-1)
#     print(ans[0])
#     return

# q = int(input())
# for i in range(q):
#     main()



# WA
# def main():
#     s = list(input().rstrip())
#     t = list(input().rstrip())
#     # print(s)
#     # print(t)
#     ans = "NO"
#     if len(s)<len(t):
#         print(ans)
#         return
#     for i in range(len(s)-1, -1, -1):
#         if s[i]!=t[-1]: continue
#         si = i
#         for ti in range(len(t)-1, -1, -1):
#             while si>=0 and s[si]!=t[ti]:
#                 si -= 2
#             si -= 1
#             if si<ti: break
#         else:
#             ans = "YES"
#             break
#     print(ans)
#     return
 
# q = int(input())
# for i in range(q):
#     main()