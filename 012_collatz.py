def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number +1

print('Enter a number: ')   
num = int(input())
while True:
    num = collatz(num)
    print(str(num))
    if num == 1:
        break
print(str(num))

# Running result:
# Enter a number:
# 3
# 10
# 5
# 16
# 8
# 4
# 2
# 1
# 1