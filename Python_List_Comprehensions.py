#Performing Mathematical Operations on the entire List

list1=[1,2,3,4,5,7,8,9,10]
newlist1=[x**2 for x in list1] #Performing square of the list1
print("Square of the list 1 is: ",newlist1)
print() #For Blank Line


#Performing conditional filtering operations on the entire list

list2=[10,11,12,13,14,15,16,17,18,19,20]
newlist2=[x for x in list2 if x%2==0] #Filter the even number in the list
newlist3=[x**2 for x in list2 if x%2==0] #Filter the even number and sqaure them
print("Even Numbers in the list 2 is: ",newlist2)
print("Sqaure of the even number in List 2 is: ",newlist3)
print()


#Combining multiple lists into one

list3=[1,2,3,4,5]
list4=[6,7,8,9,10]
newlist4=[(x + y) for (x,y) in zip(list3,list4)] #Parallel Iterators
newlist5=[(x,y) for x in list3 for y in list4] #nested iterators
newlist6=[x for x in zip(list3,list4)]
print("Parallel iterators in list 3 and list 4: ",newlist4)
print("Nested iterators in list 3 and list 4: ",newlist5)
print("Combining list items 1 with list items 2: ",newlist6)
print()

#Flatenning a Multidimensional Array
#Flatenning means reshaping the Multidimensional Array in 1-D Array
list5=[[10,20,30],[40,50,60],[70,80,90]]
newlist7 = [x for temp in list5 for x in temp]
print("Flatenning list 5 in 1 Dimension: ",newlist7)
