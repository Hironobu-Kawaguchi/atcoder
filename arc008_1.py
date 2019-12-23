# https://atcoder.jp/contests/arc008/tasks/arc008_1

N = int(input())
ans = min((N//10)*100 + (N%10)*15, (N//10+1)*100)
print(ans)
