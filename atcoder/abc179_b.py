# https://atcoder.jp/contests/abc179/tasks/abc179_b

def main():
    n = int(input())
    cnt = 0
    for i in range(n):
        a, b = map(int, input().split())
        if a==b: cnt += 1
        else: cnt = 0
        if cnt==3:
            print("Yes")
            return
    print("No")
    return

main()



# n = int(input())
# max_cnt = 0
# cnt = 0
# for i in range(n):
#     d1, d2 = map(int, input().split())
#     if d1==d2:
#         cnt += 1
#     else:
#         max_cnt = max(max_cnt, cnt)
#         cnt = 0
# max_cnt = max(max_cnt, cnt)
# if max_cnt >= 3:
#     print('Yes')
# else:
#     print('No')
