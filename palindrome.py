# Find the word is palindrome or not

name = str(input("Enter a name :"))
if name == name[::-1]:
    print("Palindrome !!!")
else:
    print(" Not Palindrome...")
