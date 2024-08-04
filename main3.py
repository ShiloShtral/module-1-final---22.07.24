sum_num = 0
first_input = True

while True:
    num = int(input("Enter a number , Enter -99 to exit : "))
    if first_input and num == -99:
        print("None")
        break

    first_input = False

    if num == -99:
        break
    sum_num += num
print(f"The numbers are : {sum_num}")

############################################################### 2
max = None
min = None
first_input = True

while True:
    num = int(input("Enter a number : "))
    if first_input and num <= -99:
         print("None")
         break

    first_input = False

    if num <= 0:
        break

    if max is None or num > max:
        max = num

    if min is None or num < min:
        min = num

if max is not None and min is not None:
    print(f"The largest number is {max}")
    print(f"The smallest number is {min}")

############################################################### 3

index = 0
max_num = None

list1 = []
for i in range(1, 6):
    num = int(input("Enter a number : "))
    list1.append(num)

max_num = max(list1)
index = list1.index(max_num)

print(f"The highest number is {max_num} and its position is {index}")

############################################################### 4

# את תרגיל 4 לא הצלחתי לעשות חוץ מלקלוט מסםרים....

############################################################### 5
result = 0

num1 = int(input("Enter a number : "))
num2 = int(input("Enter a number : "))

result = num1 ** num2

print(f"The result is : " , result)

############################################################### 6

num = input("Enter a three digits number : ")
dig = input("Enter a one digit number : ")

if dig in num :
    print(True)
else:
    print(False)
