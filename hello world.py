def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y







print("select operation")
print("1 to add")
print("2 to subtract")
print("3 to multiply")
print("4 to divide")
print("5 to pop and print values1")
print("6 to pop and print values6")


choice = input("Enter the operation")

num1 = float(input("First number"))
num2 = float(input("Second number"))



if choice == '1':
    print(add(num1, num2))

elif choice=='2':
    print(subtract(num1,num2))

elif choice=='3':
    print(multiply(num1, num2))

elif choice =='4':
    print(divide(num1,num2))

else:
    print("Error")