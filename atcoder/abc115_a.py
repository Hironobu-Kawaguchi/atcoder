# A - Christmas Eve Eve Eve
# https://atcoder.jp/contests/abc115/tasks/abc115_a
"""
とある世界では、今日は 12 月 D 日です。
D=25 なら Christmas, D=24 なら Christmas Eve, D=23 なら Christmas Eve Eve, D=22 なら Christmas Eve Eve Eve と出力するプログラムを作ってください
print('Christmas' + ' Eve' * (25 - int(input())))
"""
D = int(input())
res = 'Christmas' + ' Eve' * (25 - D)
print(res)