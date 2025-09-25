# N面サイコロをM回振ったときの結果を表示してください
# N, M は正の整数とします
# N, M はユーザーからの入力を利用すること

import random

n = int(input("サイコロの面の数は?: "))
m = int(input("何回振りますか?: "))

results = []
for _ in range(m):
    roll = random.randint(1, n)
    results.append(roll)

print(results)
