# 出力するテキストファイルの名前を定義
filename = "seeds_add.txt"

# ファイルを書き込みモードで開く
with open(filename, "w") as f:
    # 0から999までの数字を繰り返し
    Ss = [i*i for i in range(1, 31)]
    Ls = [15, 25, 35, 45]
    Ns = [65, 75, 85, 95]
    for i in range(100 + 30*4*4):
        # 数字をファイルに書き込む
        si = (i-100)//16%30
        li = (i-100)//4%4
        ni = (i-100)%4
        if i<100:
            f.write(f"{i}\n")
        else:
            f.write(f"{i} {Ls[li]} {Ns[ni]} {Ss[si]}\n")

print(f"Numbers written to {filename}")
