# 下記のコードが期待通り動作するような、dice() 関数を実装してください
# dice() 関数は 1 から 6 の整数をランダムに返す
import random


def dice():
    return random.randint(1, 6)


print(dice())
