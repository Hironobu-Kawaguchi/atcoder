# https://atcoder.jp/contests/language-test-202001/tasks/abc086_a

a, b = map(int, input().split())
if a&1 and b&1:
    print("Odd") 
else:
    print("Even")
