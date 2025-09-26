class Customer:
    def __init__(self, first_name: str, family_name: str, age: int) -> None:
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self) -> str:
        return f"{self.first_name} {self.family_name}"

    def entry_fee(self) -> int:
        if self.age <= 3:
            return 0
        if self.age < 20:
            return 1000
        if self.age < 65:
            return 1500
        if self.age < 75:
            return 1200
        return 500

    def info_csv(self) -> str:
        return f"{self.full_name()},{self.age},{self.entry_fee()}"

    def info_tab(self) -> str:
        return f"{self.full_name()}\t{self.age}\t{self.entry_fee()}"

    def info_pipe(self) -> str:
        return f"{self.full_name()}|{self.age}|{self.entry_fee()}"


if __name__ == "__main__":
    ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
    tom = Customer(first_name="Tom", family_name="Ford", age=57)
    ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=75)
    michelle = Customer(first_name="Michelle", family_name="Tanner", age=3)

    print(ken.info_pipe())
    print(tom.info_pipe())
    print(ieyasu.info_pipe())
    print(michelle.info_pipe())
