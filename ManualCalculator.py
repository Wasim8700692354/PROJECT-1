    #Python program for simple calculator

#Function to add two numbers.
def add(num1, num2):
    return num1+num2

#Function to sub two numbers.
def subtract(num1, num2):
    return num1-num2

#Function to mul two numbers.
def multiply(num1, num2):
    return num1*num2

#Function to div two numbers.
def divide(num1, num2):
    return num1/num2

print("Please select operation...\n"\
    "1. Add\n"\
    "2. Subtract\n"\
    "3. Multipy\n"\
    "4. Divide\n")

# Take input from the user
select=int(input("select operation from 1,2,3,4: "))

number_1=float(input("Enter the number: "))

number_2=float(input("Enter the number: "))

if select==1:
    print(number_1,"+",number_2,"=",add(number_1,number_2))

elif select==2:
    print(number_1,"-",number_2,"=",subtract(number_1,number_2))

elif select==3:
    print(number_1,"*",number_2,"=",multiply(number_1,number_2))

elif select==4:
    print(number_1,"/",number_2,"=",divide(number_1,number_2))

else:
    print("invalid input")
