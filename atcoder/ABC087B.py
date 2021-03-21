"""
問題文
あなたは、500 円玉を A 枚、100 円玉を B 枚、50 円玉を C 枚持っています。 これらの硬貨の中から何枚かを選び、合計金額をちょうど X 円にする方法は何通りありますか。
同じ種類の硬貨どうしは区別できません。2 通りの硬貨の選び方は、ある種類の硬貨についてその硬貨を選ぶ枚数が異なるとき区別されます。
制約
0≤A,B,C≤50
A+B+C≥1
50≤X≤20,000
A,B,C は整数である
X は 50 の倍数である
"""
a = int(input())
b = int(input())
c = int(input())
x = int(input())
num = 0
for i in range(a + 1):
    for j in range(b + 1):
        rest = x - (i * 500 + j * 100)
        if rest >= 0 and rest / 50 <= c:
            num += 1
print(num)
