def main():
    rows = int(input("行数を入力してください: "))
    cols = int(input("列数を入力してください: "))

    for i in range(1, rows + 1):
        line = ""
        for j in range(1, cols + 1):
            result = i * j
            line += f"{i} x {j} = {result:2} | "
        print(line)


if __name__ == "__main__":
    main()
