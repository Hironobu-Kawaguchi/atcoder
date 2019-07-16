"""
ABC086C - Traveling
シカのAtCoDeerくんは二次元平面上で旅行をしようとしています。
AtCoDeerくんの旅行プランでは、時刻 0 に 点 (0,0) を出発し、 1 以上 N 以下の各 i に対し、時刻 ti に 点 (xi,yi) を訪れる予定です。
AtCoDeerくんが時刻 t に 点 (x,y) にいる時、 時刻 t+1 には 点 (x+1,y), (x−1,y), (x,y+1), (x,y−1) のうちいずれかに存在することができます。 
その場にとどまることは出来ないことに注意してください。 AtCoDeerくんの旅行プランが実行可能かどうか判定してください。
"""
"""
N = int(input())
for i in range(N):
  t, x, y = map(int, input().split())
  if t < x + y or (t - x - y) % 2 == 1:
    print('No')
    exit()
print('Yes')
"""
N = int(input())
for i in range(N):
    t, x , y = map(int, input().split())
    if t < x + y or (t - x - y) % 2 == 1:
        print('No')
        exit()
print('Yes')