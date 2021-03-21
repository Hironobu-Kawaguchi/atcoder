# https://atcoder.jp/contests/abc031/tasks/abc031_c

N = int(input())
a = list(map(int, input().split()))

ans = [0] * N           # 高橋君の得点
for i in range(N):      # 高橋君
    aoki = -10000       # 青木君の得点
    takahashi = a[i]    # 高橋君の得点
    for j in range(N):  # 青木君
        if i == j:
            continue
        elif i > j:
            T = a[j:i+1]
        elif i < j:
            T = a[i:j+1]
        tmp = sum(T[1::2])
        if tmp > aoki:
            aoki = tmp
            takahashi = sum(T[0::2])
            # best_j = j
    ans[i] = takahashi
    # print(i, takahashi, best_j, aoki)
# print(ans)
print(max(ans))
