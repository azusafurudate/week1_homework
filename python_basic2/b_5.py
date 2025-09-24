# スペース区切りで入力された整数群において、以下の4つの統計量を計算アプリを実装してください
# ただし、計算用の組み込み関数やライブラリは使わないこと(sum()やnp.mean()などはNG print()はOK)
# 1つの統計量につき、それ専用の関数を実装すること


# 合計値
def total(numbers):
    value = 0
    for n in numbers:
        value = value + n
    return value

# 最大値
def max(numbers):
    maximum = numbers[0]
    for n in numbers:
        if n > maximum:
            maximum = n
    return maximum

# 最小値
def min(numbers):
    minimum = numbers[0]
    for n in numbers:
        if n < minimum:
            minimum = n
    return minimum

# 平均値
def average(numbers):
    value = total(numbers)
    count = 0
    for _ in numbers:
        count = count + 1
    return value // count


data = input("Data (space separated) > ")

numbers = []
for text in data.split():
    numbers.append(int(text))

print("total:", total(numbers))
print("max:", max(numbers))
print("min:", min(numbers))
print("average:", average(numbers))
