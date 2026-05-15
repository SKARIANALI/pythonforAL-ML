list1=[]
print(type(list1))

list2=[10,20,'arian',10,20]
print(list2)

list3=list() #list() func
print(list3)
print(type(list3))

list4=[10,20,'ankush']
print(list4[2]) #indexing
print(list4[0:3]) #slicing perform list -1

#count() method...

list5=[10,20,'ankush']
print(list5.count('ankush')) #count() method...
print(list2.count(10))

print(list2.index('arian')) #index() method....
print(list2.index(10))
print(list2.index(10,1)) # except pos 0 searching starts from pos 1

list4.insert(2,'arian') #insertion (pos+ element) which we add in the list
print(list4)

list4.pop(2) #deletion
print(list4)

list4.pop() # pop last element in the list 
print(list4)

#extend list ...

list6=[10,20,30]
list6.extend(['arian']) 
print(list6)
list6.extend('subham')
print(list6)


list7=['fardeen','ankush'] #create new list to extend 
list6.extend(list7)
print(list6)

#copy method...

list8=list7.copy()
print(list8)

list8=list7[:] #[0:n-1] list copy
print(list8)

#sort method...

list9=[10,50,70,90,20]
list9.sort()
print(list9)
list9.sort(reverse=True) # decending order
print(list9)


#reverse method 

list10=[10,50,70,90,20]
list10.reverse()
print(list10)

list11=[10,20,30,['arian','ankush',[20.75,75.0]]] #Nested list
print(list11)

#list comprehension 

list12=['ankush','arian','suman']
x=[word for word in list12 if word.startswith('a')]
print(x)

#list unpacking...

list13=['ankush','arian']
a,b=list13
print(a)
print(b)

list14=[10,20]
a,b=list14
print(a+b)
