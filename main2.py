top = int(input("Enter a positive integer: "))

if top > 0:
    for number in range(1, top + 1):
        print(number)
else:
    print("Please enter a positive integer.")
################################################ 2
top2 = int(input("Enter a integer : "))
top3 = int(input("Enter a integer : "))

if top2 < top3:
    for i in range(top2, top3 + 1):
        print(i)
elif top2 > top3:
    for g in range(top3, top2 + 1):
        print(g)
################################################ 3

n = int(input("Enter a integer : "))

if n > 0 and n % 2 == 0:
    for i in range(0, n + 1, 2):
        print(i)
################################################ 4

max = int(input("Enter the max integer : "))
den = int(input("Enter a dem integer : "))

if max > 0 and den > 0:
    for i in range(den, max + 1, den):
        if i % den == 0:
           print(i)

else:
    print("Both numbers must be positive integers")