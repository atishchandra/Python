#Calculator using Fundamentals of Python

def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2

print("**********")
print("Please Choose a operation")
print("+")
print("-")
print("*")
print("/")
print("***********")

choice=input("Enter your Operation")
num1=int(input("Enter the first Number"))
num2=int(input("Enter the Second Number"))
        
if choice=='+':
    print(num1, "+", num2, "=", add(num1,num2))

elif choice == '-':
    print(num1, "-", num2, "=", sub(num1, num2))

elif choice == '*':
    print(num1, "*", num2, "=", mul(num1, num2))

elif choice == '/':
    print(num1, "/", num2, "=", div(num1, num2))
            
else:
    print('Please Enter a Valid Input!')
