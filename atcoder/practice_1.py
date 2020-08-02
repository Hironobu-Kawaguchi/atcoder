"""
A - はじめてのあっとこーだー（Welcome to AtCoder）
https://practice.contest.atcoder.jp/tasks/practice_1
高橋君はデータの加工が行いたいです。
整数 a,b,cと、文字列 s が与えられます。
整数 a+b+c と、文字列 s を並べて表示しなさい。
"""
a = int(input())
b, c = map(int, input().split())
s = input()
print("{} {}".format(a+b+c, s))