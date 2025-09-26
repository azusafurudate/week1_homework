# 課題D-1: 円オブジェクト
# 次のコードが正しく動作するような Circle クラスを実装してください
# area は面積、 perimeter は周囲長(=円周の長さ) という意味です。

class Circle:
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        return 3.14 * (self.radius**2)

    def perimeter(self) -> float:
        return 2 * 3.14 * self.radius


if __name__ == "__main__":
    print("Hello")  

# 半径1の円
circle1 = Circle(radius=1)
print(circle1.area())  # 3.14
print(circle1.perimeter())  # 6.28

# 半径3の円
circle3 = Circle(radius=3)
print(circle3.area())  # 28.27
print(circle3.perimeter())  # 18.85
