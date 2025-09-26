# 課題D-2: 長方形オブジェクト
# 次のコードが正しく動作するような Rectangle クラスを実装してください
# diagonal は 対角線(の長さ) という意味です。

import math


class Rectangle:
    def __init__(self, height: float, width: float) -> None:
        self.height = height
        self.width = width

    def area(self) -> float:
        return self.height * self.width

    def diagonal(self) -> float:
        return math.sqrt(self.height**2 + self.width**2)


if __name__ == "__main__":
    rectangle1 = Rectangle(height=5, width=6)
    print(f"{rectangle1.area():.2f}")  # 30.00
    print(f"{rectangle1.diagonal():.2f}")  # 7.81

    rectangle2 = Rectangle(height=3, width=3)
    print(f"{rectangle2.area():.2f}")  # 9.00
    print(f"{rectangle2.diagonal():.2f}")  # 4.24
