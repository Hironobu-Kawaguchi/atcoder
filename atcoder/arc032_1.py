# https://atcoder.jp/contests/arc032/tasks/arc032_1

n = int(input())
if n == 2:
    ans = "WANWAN"
else:
    ans = "BOWWOW"
print(ans)


# n = int(input())
# num = n*(n+1)//2
# if num == 1:
#     ans = "BOWWOW"
# else:
#     ans = "WANWAN"
# for i in range(2, int(num**0.5)+1):
#     if num%i == 0:
#         ans = "BOWWOW"
#         break
# print(ans)
