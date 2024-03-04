# Find the factorial
# using for loop
x = int(input("Enter a number :"))
total = 1
for i in range(1,x+1):
    total = total * i
    print(total)

# using while loop find factorial
y = int(input("Enter a number :"))
total1 = 1
count = 1
while count <= y:
    total1 = total1 * count
    print(total1)
    count +=1


