# https://atcoder.jp/contests/abc146/tasks/abc146_b

N = int(input())
S = input()

ans = ''
for s in S:
    idx = ord(s)- ord("A")
    idx = (idx + N) % 26
    ans += chr(idx + ord("A"))

print(ans)
