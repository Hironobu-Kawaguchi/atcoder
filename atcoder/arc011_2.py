# https://atcoder.jp/contests/arc011/tasks/arc011_2

N = input()
words = input().split()
rule = 'zrbcdwtjfqlvsxpmhkng'
d = {}
for i in range(10):
    x,y = rule[2*i:2*i+2]
    d[x] = str(i)
    d[y] = str(i)

def convert(word):
    res = ''
    for char in word.lower():
        if char not in d:
            continue
        res += d[char]
    return res

words = [convert(word) for word in words]
words = [word for word in words if word]
print(*words)
