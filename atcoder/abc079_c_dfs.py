# C - Train Ticket
# https://atcoder.jp/contests/abc079/tasks/abc079_c

def dfs(i, f, sum):
    if i == 3:
        if sum == 7:
            # 答えは1つ出力すれば良いので =7 になれば終了
            print(f + "=7")
            exit()

    else:
        # 式 f の末尾に符号と次の数字を追加し、その分 sum に加減する
        dfs(i + 1, f + "+" + s[i + 1], sum + int(s[i + 1]))
        dfs(i + 1, f + "-" + s[i + 1], sum - int(s[i + 1]))

s = input()

dfs(0, s[0], int(s[0]))
