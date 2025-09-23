# "Bob", "Tom", "Ken" という3つの文字列要素を持つusersというリストを定義してください。
users = ["Bob","Tom","Ken"]
print(users)
# 1から5までの整数を要素として持つint_numbersリストを定義してください
int_numbers = [1,2,3,4,5]
print(int_numbers)
# "Bob", "Dylan", 79 という 3つの要素をもつbob_infoというリストを定義してください
bob_info =["Bob","Dylan",79]
print(bob_info)
# 次のmembersというリストから "Bob" と "Tom" を取得して出力してください
members = ["Bob", "Tom", "Ken"]
print(members[0])  
print(members[1])
# 次のmembersというリストから "Bob" と "Tom" を取得して、それぞれ1件ずつ、"Bob" と "Tom"を出力してください
print(members[0])
print(members[1])
# 次のリストを利用して、"Name: Bob Dylan, Age: 79"と出力してください
bob_info = ["Bob", "Dylan", 79]
print(f"Name: {bob_info[0]} {bob_info[1]}, Age: {bob_info[2]}")
# for を使って odd_numbers の各要素を出力してください
odd_numbers = [1, 3, 5, 7, 9]
for num in odd_numbers:
    print(num)
# for を使って even_numbers のそれぞれの値を2倍した値を出力してください
even_numbers = [2, 4, 6, 8]
for num in even_numbers:
    print(num * 2)
# users_info を使って次のような出力をしてください
# Name: Bob, Age: 79
# Name: Tom, Age: 59
# Name: Ken, Age: 61
users_info = [["Bob", 79], ["Tom", 59], ["Ken", 61]]
for user in users_info:
    print(f"Name: {user[0]}, Age: {user[1]}")
# 下記のコードが期待通り動作するような辞書を定義してください
# print(bob_info["first_name"])  # "Bob"
# print(bob_info["family_name"])  # "Dylan"
# print(bob_info["age"])  # 79
bob_info = {"first_name": "Bob", "family_name": "Dylan", "age": 79}
print(bob_info["first_name"])  # Bob
print(bob_info["family_name"])  # Dylan
print(bob_info["age"])  # 79
# 下記のコードが期待通り動作するような、dice() 関数を実装してください ※ dice()関数は1から6の整数をランダムに返す
import random
def dice():
    return random.randint(1, 6)
print(dice())
