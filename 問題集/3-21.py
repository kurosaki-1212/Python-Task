import random
num1 = random.randint(0,9)
num2 = random.randint(0,9)
num3 = random.randint(0,9)
num4 = random.randint(0,9)

print(str(num1) + " + " + str(num2) + " * " + str(num3) + " - " + str(num4) + " = ")
suzi = num1 + num2 * num3 - num4
kei = int(input("計算結果は？："))

if suzi == kei:
    print("正解です")
else:
    print("不正解です")