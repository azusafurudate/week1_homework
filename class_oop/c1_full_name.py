class Customer:
    def __init__(self, first_name: str, family_name: str) -> None:
        self.first_name = first_name
        self.family_name = family_name

    def full_name(self) -> str:
        return f"{self.first_name} {self.family_name}"


if __name__ == "__main__":
    ken = Customer(first_name="Ken", family_name="Tanaka")
    tom = Customer(first_name="Tom", family_name="Ford")
    ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa")

    print(ken.full_name())
    print(tom.full_name())
    print(ieyasu.full_name())
