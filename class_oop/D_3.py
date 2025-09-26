# 課題D-3: 正方形オブジェクト
# 次のコードが正しく動作するような Square クラスを実装してください
# diagonal は 対角線(の長さ) という意味です。

import math


class Square:
    def __init__(self, side: float) -> None:
        self.side = side

    def area(self) -> float:
        return self.side * self.side

    def diagonal(self) -> float:
        return math.sqrt(2) * self.side


if __name__ == "__main__":
    square1 = Square(side=1.5)
    print(f"{square1.area():.2f}")  # 2.25
    print(f"{square1.diagonal():.2f}")  # 2.12

    square2 = Square(side=15)
    print(f"{square2.area():.2f}")  # 225.00
    print(f"{square2.diagonal():.2f}")  # 21.21
