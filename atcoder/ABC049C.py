"""
ABC049C - 白昼夢 / Daydream
英小文字からなる文字列 S が与えられます。 Tが空文字列である状態から始め、以下の操作を好きな回数繰り返すことで S=T とすることができるか判定してください。
T の末尾に dream dreamer erase eraser のいずれかを追加する。
"""
"""
s = input()
l = ["eraser", "erase", "dreamer", "dream"]
for c in l:
    s = s.replace(c, "")
if s == "":
    print("YES")
else:
    print("NO")
"""
S = input()
outs = "NO"
slist5 = ["dream", "erase" ]
slist6 = ["eraser"]
slist7 = ["dreamer"]
n = len(S)
while len(S) >=5:
    if S[n-5:n] in slist5:
        S = S[:n-5]
        n = n-5
    elif S[n-6:n] in slist6:
        S = S[:n-6]
        n = n-6
    elif S[n-7:n] in slist7:
        S = S[:n-7]
        n = n-7
    else:
        break
    if len(S) == 0:
        outs = "YES"
print(outs)