# https://codeforces.com/contest/1459/problem/B

nums = [1]
for i in range(1, 1001):
    cnt = ((i+1)//2) * 4
    nums.append(cnt)

n = int(input())
ans = 0
for i in range(n+1):
    if i%2!=n%2: continue    ### 偶奇が違う
    if i%2==0 and i%4!=n%4: continue   ### 偶数で mod 4が違う
    ans += nums[i]
print(ans)
