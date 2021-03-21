# https://atcoder.jp/contests/abc035/tasks/abc035_a

W, H = map(int, input().split())
if W * 3 == H * 4:
    print("4:3")
elif W * 9 == H * 16:
    print("16:9")
    