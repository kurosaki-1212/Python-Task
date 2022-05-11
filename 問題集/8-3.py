Find = []
Buzz = []

for i in range(10):
    num = (int(input(str(i + 1) + "件目：整数を入力＝")))
    if num % 2 == 0:
        Find.append(num)
    else:
        Buzz.append(num)

print("偶数値配列＝",Find)
print("奇数値配列＝",Buzz)