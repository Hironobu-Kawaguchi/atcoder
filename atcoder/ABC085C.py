"""
ABC085C - Otoshidama
日本でよく使われる紙幣は、10000 円札、5000 円札、1000 円札です。以下、「お札」とはこれらのみを指します。
青橋くんが言うには、彼が祖父から受け取ったお年玉袋にはお札が N 枚入っていて、合計で Y 円だったそうですが、嘘かもしれません。
このような状況がありうるか判定し、ありうる場合はお年玉袋の中身の候補を一つ見つけてください。なお、彼の祖父は十分裕福であり、お年玉袋は十分大きかったものとします。
10 * n1 + 5 * n2 + n3 = Y
n1 + n2 + n3 = N
-> n2 = (Y - N - 9 * n1) / 4
"""
N, Y = map(int, input().split())
Y = Y/1000
n1, n2, n3 = -1, -1, -1
for i in range(N+1):
    k5 , mod = divmod((Y - N - 9*i) , 4)
    if mod==0 and k5>=0 and i+k5<=N:
        n1 = i
        n2 = int(k5)
        n3 = N - n1 - n2
        break
print(n1, n2, n3)