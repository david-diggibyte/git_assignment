# Find the factorial
# using for loop
num = int(input("Enter a number :"))
total = 1
for i in range(1,num+1):
    total = total * i
    print(total)

# using while loop find factorial
num1 = int(input("Enter a number :"))
total1 = 1
count = 1
while count <= num1:
    total1 = total1 * count
    print(total1)
    count +=1
# added one line for fetch purpose



