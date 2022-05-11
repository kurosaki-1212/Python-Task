from typing import OrderedDict


print("0~100までの得点（整数値）を２つ入力してください")
n = int(input("１つ目の得点："))
m = int(input("２つ目の得点："))
if n >= 80 and m >= 80:
    print("２科目とも合格です")