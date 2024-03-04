# Find the word is palindrome or not

n = str(input("Enter a name :"))
if n == n[::-1]:
    print(f"{n} is Palindrome !!!")
else:
    print(f"{n} is Not Palindrome...")
