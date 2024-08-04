x = float(input("Enter float number : "))
y = float(input("Enter float number : "))

find_smaller = min(x, y)
for _ in range(3):
    print(find_smaller)
####################################################### 2
intnum = int(input("Enter an int number : "))
intnum2 = int(input("Enter an int number : "))
intnum3 = int(input("Enter an int number : "))

find_bigger = max(intnum, intnum2, intnum3)
print(find_bigger)
####################################################### 3
movielen = int(input("What is the length of the movie in minutes : "))
hours = movielen // 60
minutes = movielen % 60

print(f"the length of the movie is {hours} hours and {minutes} minutes.")
####################################################### 4

number_4 = input("Enter a number higher then 999 : ")
print(number_4[-1])

number_4 = input("Enter a number higher then 999 : ")
print(number_4[-2])
####################################################### 5

sum1 = int(input("Enter a number smaller then 100 : "))
sum2 = int(input("Enter a number smaller then 100 : "))

print(f"The sum of entered numbers is {sum1}{sum2}")
####################################################### 6

flipnum = (input("Enter a two digit number : "))
print("The number after we flip the digits is ", flipnum[::-1])
####################################################### 7

evenodd = int(input("Enter number : "))
if evenodd % 10 == 0:
    print("The number is even")
else:
    print("The number is odd")

####################################################### 8

payment = int(input("Enter your last payment in dollars : "))
tax = (payment * 10 ) / 100

if payment > 6000 and payment <= 12000:
    print(f"You need to pay {tax} dollars tax .")

tax = (payment * 20 ) / 100
if payment in range(12000, 18000):
    print(f"you need to pay {tax} dollars tax .")

tax = (payment * 30) / 100
if payment in range(18001, 25000):
    print(f"you need to pay {tax} dollars tax .")

tax = (payment * 40) / 100
if payment in range(25001, 35000):
    print(f"you need to pay {tax} dollars tax .")

tax = (payment * 45) / 100
if payment in range(35001, 5000):
    print(f"you need to pay {tax} dollars tax .")

tax = (payment * 51) / 100
if payment > 50001:
    print(f"you need to pay {tax} dollars tax .")
####################################################### 9

age = int(input("Enter your age : "))
height = int(input("Enter your height in centimeters: "))

if age in range(8, 18) and height > 100:
    print("You can get on the roller coaster")

elif age > 18 and height > 100:
    print("You can get on the roller coaster")

else:
    print("You cant get on the roller coaster")