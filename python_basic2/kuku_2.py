# 下記のような出力が得られる kuku_2.py を実装してください
# 任意の行数および任意の列数での掛け算の結果が得られます
# $ python kuku_2.py
# 行数を入力してください: 4
# 列数を入力してください: 6
# 1 2 3 4 5 6
# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24

rows = int(input("行数を入力してください: "))
cols = int(input("列数を入力してください: "))

for i in range(1, rows + 1):
    for j in range(1, cols + 1):
        print(i * j, end=" ")
    print()





