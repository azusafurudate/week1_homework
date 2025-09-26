class Customer:
    def __init__(self, first_name: str, family_name: str, age: int) -> None:
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self) -> str:
        return f"{self.first_name} {self.family_name}"


if __name__ == "__main__":
    ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
    tom = Customer(first_name="Tom", family_name="Ford", age=57)
    ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=75)

    print(ken.age)
    print(tom.age)
    print(ieyasu.age)
