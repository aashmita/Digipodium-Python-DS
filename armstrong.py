num = int(input("Enter a number"))
original = num
digits = len(str(num))

sum_of_powers = 0

while num>0:
    digit = num%10
    sum_of_powers += digit ** digits
    num = num // 10

if original == sum_of_powers:
    print("Armstrong number")
else:
    print("Not Armstrong Number")