#Quadratic-Roots
import cmath
a=int(input("Enter the first value: "))
b=int(input("Enter the second value: "))
c=int(input("Enter the third value: "))
d=(b**2)-(4*a*c)
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)
print("Sol: ",sol1)
print("Sol: ",sol2)
