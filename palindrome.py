# Find the word is palindrome or not

n = str(input("Enter a name :"))
if n == n[::-1]:
    print("Palindrome !!!")
else:
    print(" Not Palindrome...")
