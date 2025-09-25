# スペース区切りで入力された整数群において、以下の4つの統計量を計算アプリを実装してください
# ただし、計算用の組み込み関数やライブラリは使わないこと(sum()やnp.mean()などはNG print()はOK)
# 1つの統計量につき、それ専用の関数を実装すること


# 合計値
def 合計値(numbers):
    value = 0
    for n in numbers:
        value = value + n
    return value

# 最大値
def 最大値(numbers):
    maximum = numbers[0]
    for n in numbers:
        if n > maximum:
            maximum = n
    return maximum

# 最小値
def 最小値(numbers):
    minimum = numbers[0]
    for n in numbers:
        if n < minimum:
            minimum = n
    return minimum


# 平均値
def 平均値(numbers):
    value = 合計値(numbers)
    count = 0
    for _ in numbers:
        count = count + 1
    return value // count


data = input("Data (スペース区切り) > ")

numbers = []
for text in data.split():
    numbers.append(int(text))

print("合計値:", 合計値(numbers))
print("最大値:", 最大値(numbers))
print("最小値:", 最小値(numbers))
print("平均値:", 平均値(numbers))
