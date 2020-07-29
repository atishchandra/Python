#Area of Triangle--Heron's Formula--When three Side is Given
a=int(input("Enter the first side: "))
b=int(input("Enter the second side: "))
c=int(input("Enter the third side: "))
s=a+b+c/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("Area of the given Triangle is: ",area)
