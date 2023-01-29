# https://atcoder.jp/contests/arc127/tasks/arc127_a

# import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N = input()
ans = 0
for i in range(len(N)):
    for j in range(1, len(N)+1-i):
        if i==0:
            if int(N[:j])<int('1'*j): 
                continue
            elif  int(N[:j])==int('1'*j):
                ans += int('0'+N[j:]) + 1
            else:
                ans += 10**(len(N)-j)
        else:
            ans += 10**(len(N)-j-i)
        # print(i, j, ans)
print(ans)
