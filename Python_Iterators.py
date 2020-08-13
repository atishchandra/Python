#Example1

mylist=[1,2,3,4,5]
print(mylist)
x=iter(mylist)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))

#Output1
'''

[1, 2, 3, 4, 5]
1
2
3
4
5

'''

print()
#Example2

myname="Atish Chandra"
iter_obj=iter(myname)

while True:
    try:
        item=next(iter_obj)
        print(item)
    except StopIteration:
        break
        
#output1
'''
A
t
i
s
h
 
C
h
a
n
d
r
a
'''
print()
#Example3

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

#output3

'''
1
2
3
4
5
'''
