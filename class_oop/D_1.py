import numpy as np

# 課題D-1: 円オブジェクト
# 次のコードが正しく動作するような Circle クラスを実装してください
# area は面積、 perimeter は周囲長(=円周の長さ) という意味です。

class Circle:
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        return float(np.pi) * (self.radius**2)

    def perimeter(self) -> float:
        return 2 * float(np.pi) * self.radius

# 半径1の円
circle1 = Circle(radius=1)
print(round(circle1.area(), 2))  # 3.14
print(round(circle1.perimeter(), 2))  # 6.28

# 半径3の円
circle3 = Circle(radius=3)
print(round(circle3.area(), 2))  # 28.27
print(round(circle3.perimeter(), 2))  # 18.85
