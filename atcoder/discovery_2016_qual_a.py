# https://atcoder.jp/contests/discovery2016-qual/tasks/discovery_2016_qual_a

s = 'DiscoPresentsDiscoveryChannelProgrammingContest2016'
w = int(input())
n = (len(s)+w-1)//w

for i in range(n):
    print(s[i*w:min((i+1)*w,len(s))])
