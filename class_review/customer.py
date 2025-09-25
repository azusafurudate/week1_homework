# 下記の雛形を利用して、各問のコードが期待通り動作するようなCustomerクラスを実装してください
# class Customer
# 各問のコードが期待通り動作するように実装
# pass
# ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
# tom = Customer(first_name="Tom", family_name="Ford", age= 57)
# ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=75)
# 以降で各問のコードを追加していく
class Customer:
    def __init__(self, first_name: str, family_name: str, age: int):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age


ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
tom = Customer(first_name="Tom", family_name="Ford", age=57)
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=75)

print(ken.first_name, ken.family_name, ken.age)
print(tom.first_name, tom.family_name, tom.age)
print(ieyasu.first_name, ieyasu.family_name, ieyasu.age)


# cー1. フルネームを取得できる
# print(ken.full_name())  # "Ken Tanaka" という値を出力
# print(tom.full_name())  # "Tom Ford" という値を出力
# print(ieyasu.full_name())  # "Ieyasu Tokugawa" という値を出力
class Customer:
    def __init__(self, first_name: str, family_name: str):
        self.first_name = first_name
        self.family_name = family_name

    def full_name(self) -> str:
        return f"{self.first_name} {self.family_name}"


ken = Customer(first_name="Ken", family_name="Tanaka")
tom = Customer(first_name="Tom", family_name="Ford")
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa")

print(ken.full_name())  # Ken Tanaka
print(tom.full_name())  # Tom Ford
print(ieyasu.full_name())  # Ieyasu Tokugawa


# C-2. 年齢という概念の追加
# print(ken.age)  # 15 という値を出力
# print(tom.age)  # 57 という値を出力
# print(ieyasu.age)  # 75 という値を出力
class Customer:
    def __init__(self, first_name: str, family_name: str, age: int):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age


ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
tom = Customer(first_name="Tom", family_name="Ford", age=57)
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=75)

print(ken.age)
print(tom.age)
print(ieyasu.age)


# C-3. 年齢に応じた適切な入場料(entry_fee)を計算できる
# 料金の計算ルール　こども料金(20歳未満): 1000円　おとな料金(20歳以上65歳未満): 1500円　シニア料金(65歳以上): 1200円
# print(ken.entry_fee())  # 1000 という値を出力
# print(tom.entry_fee())  # 1500 という値を出力
# print(ieyasu.entry_fee())  # 1200 という値を出力
class Customer:
    def __init__(self, first_name: str, family_name: str, age: int):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def entry_fee(self) -> int:
        if self.age < 20:
            return 1000
        elif self.age < 65:
            return 1500
        else:
            return 1200


ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
tom = Customer(first_name="Tom", family_name="Ford", age=57)
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=75)

print(ken.entry_fee())  # 1000
print(tom.entry_fee())  # 1500
print(ieyasu.entry_fee())  # 1200


# C-4. 単一の顧客情報をCSV形式で取得できる
# print(ken.info_csv())  # "Ken Tanaka,15,1000" という値を出力
# print(tom.info_csv())  # "Tom Ford,57,1500" という値を出力
# print(ieyasu.info_csv())  # "Ieyasu Tokugawa,75,1200" という値を出力
class Customer:
    def __init__(self, first_name: str, family_name: str, age: int):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self) -> str:
        return f"{self.first_name} {self.family_name}"

    def entry_fee(self) -> int:
        if self.age < 20:
            return 1000
        elif self.age < 65:
            return 1500
        else:
            return 1200

    def info_csv(self) -> str:
        return f"{self.full_name()},{self.age},{self.entry_fee()}"


ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
tom = Customer(first_name="Tom", family_name="Ford", age=57)
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=75)

print(ken.info_csv())
print(tom.info_csv())
print(ieyasu.info_csv())


# C-5. 3歳以下の入場料金の無料化
class Customer:
    def __init__(self, first_name: str, family_name: str, age: int):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def entry_fee(self) -> int:
        if self.age <= 3:
            return 0
        elif self.age < 20:
            return 1000
        elif self.age < 65:
            return 1500
        else:  # 65歳以上
            return 1200


ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
tom = Customer(first_name="Tom", family_name="Ford", age=57)
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=75)
michelle = Customer(first_name="Michelle", family_name="Tanner", age=3)

print(ken.entry_fee())
print(tom.entry_fee())
print(ieyasu.entry_fee())
print(michelle.entry_fee())


# C-6. 75歳以上の料金区分の追加
# 75歳以上の入場料金は500円にしてください
class Customer:
    def __init__(self, first_name: str, family_name: str, age: int):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self) -> str:
        return f"{self.first_name} {self.family_name}"

    def entry_fee(self) -> int:
        if self.age <= 3:
            return 0
        elif self.age < 20:
            return 1000
        elif self.age < 65:
            return 1500
        elif self.age < 75:
            return 1200
        else:
            return 500

    def info_csv(self) -> str:
        return f"{self.full_name()},{self.age},{self.entry_fee()}"


ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
tom = Customer(first_name="Tom", family_name="Ford", age=57)
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=75)
michelle = Customer(first_name="Michelle", family_name="Tanner", age=3)

print(ken.info_csv())
print(tom.info_csv())
print(ieyasu.info_csv())
print(michelle.info_csv())


# C-7. 単一顧客の情報取得形式の追加その1
# 単一顧客の情報取得をタブ区切りにも対応させてください
class Customer:
    def __init__(self, first_name: str, family_name: str, age: int):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self) -> str:
        return f"{self.first_name} {self.family_name}"

    def entry_fee(self) -> int:
        if self.age <= 3:
            return 0
        elif self.age < 20:
            return 1000
        elif self.age < 65:
            return 1500
        elif self.age < 75:
            return 1200
        else:
            return 500

    def info_csv(self) -> str:
        return f"{self.full_name()},{self.age},{self.entry_fee()}"

    def info_tab(self) -> str:
        return f"{self.full_name()}\t{self.age}\t{self.entry_fee()}"


ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
tom = Customer(first_name="Tom", family_name="Ford", age=57)
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=75)
michelle = Customer(first_name="Michelle", family_name="Tanner", age=3)

print(ken.info_tab())
print(tom.info_tab())
print(ieyasu.info_tab())
print(michelle.info_tab())


# C-8. 単一顧客の情報取得形式の追加その2
# 単一顧客の情報取得を「|」(パイプ)区切りにも対応させてください
class Customer:
    def __init__(self, first_name: str, family_name: str, age: int):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self) -> str:
        return f"{self.first_name} {self.family_name}"

    def entry_fee(self) -> int:
        if self.age <= 3:
            return 0
        elif self.age < 20:
            return 1000
        elif self.age < 65:
            return 1500
        elif self.age < 75:
            return 1200
        else:
            return 500

    def info_csv(self) -> str:
        return f"{self.full_name()},{self.age},{self.entry_fee()}"

    def info_tab(self) -> str:
        return f"{self.full_name()}\t{self.age}\t{self.entry_fee()}"

    def info_pipe(self) -> str:
        return f"{self.full_name()}|{self.age}|{self.entry_fee()}"


ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
tom = Customer(first_name="Tom", family_name="Ford", age=57)
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=75)
michelle = Customer(first_name="Michelle", family_name="Tanner", age=3)

print(ken.info_pipe())
print(tom.info_pipe())
print(ieyasu.info_pipe())
print(michelle.info_pipe())
