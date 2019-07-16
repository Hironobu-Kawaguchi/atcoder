"""
A - Still TBD
https://atcoder.jp/contests/abc119/tasks/abc119_a
文字列 S が入力されます。これは、西暦 2019 年の実在する日付を yyyy/mm/dd の形式で表したものです。(例えば、2019 年 4 月 30 日は 2019/04/30 と表されます。)
S が表す日付が 2019 年 4 月 30 日またはそれ以前なら Heisei、そうでなければ TBD と出力するプログラムを書いてください。
"""
S = input()
print('Heisei' if S <= '2019/04/30' else 'TBD')