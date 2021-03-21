# https://atcoder.jp/contests/abc001/tasks/abc001_3

Deg, Dis = map(int, input().split())

if Deg >= 112.5 and Deg < 337.5:
    Dir = 'NNE'
elif Deg >= 337.5 and Deg < 562.5:
    Dir = 'NE'
elif Deg >= 562.5 and Deg < 787.5:
    Dir = 'ENE'
elif Deg >= 787.5 and Deg < 1012.5:
    Dir = 'E'
elif Deg >= 1012.5 and Deg < 1237.5:
    Dir = 'ESE'
elif Deg >= 1237.5 and Deg < 1462.5:
    Dir = 'SE'
elif Deg >= 1462.5 and Deg < 1687.5:
    Dir = 'SSE'
elif Deg >= 1687.5 and Deg < 1912.5:
    Dir = 'S'
elif Deg >= 1912.5 and Deg < 2137.5:
    Dir = 'SSW'
elif Deg >= 2137.5 and Deg < 2362.5:
    Dir = 'SW'
elif Deg >= 2362.5 and Deg < 2587.5:
    Dir = 'WSW'
elif Deg >= 2587.5 and Deg < 2812.5:
    Dir = 'W'
elif Deg >= 2812.5 and Deg < 3037.5:
    Dir = 'WNW'
elif Deg >= 3037.5 and Deg < 3262.5:
    Dir = 'NW'
elif Deg >= 3262.5 and Deg < 3487.5:
    Dir = 'NNW'
else:
    Dir = 'N'

if (Dis/6*10 + 5)//10/10 >= 0.0 and (Dis/6*10 + 5)//10/10 <= 0.2:
    W = 0
    Dir = 'C'
elif (Dis/6*10 + 5)//10/10 >= 0.3 and (Dis/6*10 + 5)//10/10 <= 1.5:
    W = 1
elif (Dis/6*10 + 5)//10/10 >= 1.6 and (Dis/6*10 + 5)//10/10 <= 3.3:
    W = 2
elif (Dis/6*10 + 5)//10/10 >= 3.4 and (Dis/6*10 + 5)//10/10 <= 5.4:
    W = 3
elif (Dis/6*10 + 5)//10/10 >= 5.5 and (Dis/6*10 + 5)//10/10 <= 7.9:
    W = 4
elif (Dis/6*10 + 5)//10/10 >= 8.0 and (Dis/6*10 + 5)//10/10 <= 10.7:
    W = 5
elif (Dis/6*10 + 5)//10/10 >= 10.8 and (Dis/6*10 + 5)//10/10 <= 13.8:
    W = 6
elif (Dis/6*10 + 5)//10/10 >= 13.9 and (Dis/6*10 + 5)//10/10 <= 17.1:
    W = 7
elif (Dis/6*10 + 5)//10/10 >= 17.2 and (Dis/6*10 + 5)//10/10 <= 20.7:
    W = 8
elif (Dis/6*10 + 5)//10/10 >= 20.8 and (Dis/6*10 + 5)//10/10 <= 24.4:
    W = 9
elif (Dis/6*10 + 5)//10/10 >= 24.5 and (Dis/6*10 + 5)//10/10 <= 28.4:
    W = 10
elif (Dis/6*10 + 5)//10/10 >= 28.5 and (Dis/6*10 + 5)//10/10 <= 32.6:
    W = 11
else:
    W = 12

print(Dir, W)
