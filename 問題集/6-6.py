start = int(input("開始数"))
end = int(input("終了数"))

for i in range(start,end-1):
    start += i + 1
print(start)