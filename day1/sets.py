#Donot allow duplicate value
#Insertion order is not preserved
#Indexing & slicing not work
#Mutable
s=set() #empty set
print(type(s))
s={10,20,30,'ankush'}
print(s)

#add....
s.add('arian') #add only 1 parameter add method()...
print(s)

#update....
s.update('akash','fardeen') #update multiple par > 1 update method()...
s.update(['me','mine'])
print(s)

#pop()....
print(s.pop()) #pop() method... random pop()
print(s.pop())
print(s)

#remove()....
s1={'fardeen','arian'}
print(s1.remove('fardeen')) #choose which one we remove
print(s1)

#clear()....
s2={10,20,30}
s2.clear() #all element clear()
print(s2)

#Maths

s3={10,20,'arian','akash'}
s4={10,20,'arian','akash',50,60}

print(s3.union(s4)) #union
print(s3 | s4) #union operator

print(s3.intersection(s4)) #intersection
print(s3 & s4) #intersection operator

print(s3.difference(s4)) #difference
print(s3 - s4) #difference operator
print(s4 - s3) #difference operator

print(s3.symmetric_difference(s4)) #symmetric difference
