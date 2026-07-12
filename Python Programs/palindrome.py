num = int(input("Enter a number : "))
orig = num
reverse = 0

while num>0:
    digit = num%10
    reverse = reverse*10 + digit
    num = num // 10

print("Original number : ",orig)
print("Reverse number : ",reverse)

if(reverse == orig):
    print("Given number is palindrome number")
else:
    print("Given number is not palindrome")
    
