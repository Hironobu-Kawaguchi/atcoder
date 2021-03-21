# A - Five Antennas
# https://atcoder.jp/contests/abc123/tasks/abc123_a

l = [int(input()) for _ in range(5)]
k = int(input())
if max(l) - min(l) > k:
    print(':(')
else:
    print('Yay!')
