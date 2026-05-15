#insertion order preserved
#indexing & slicing not allowed 
#create empty dict
a={}
print(type(a))
a1=dict()
print(type(a1))


x={'age':21} #key:value
print(x)
print(x.get('age')) #using get() method..

x1={'age':21, 'roll':4 ,'name':'arian'}
print(x1)
print(x1['age']) #without using get() method...


x2={'age':21, 'roll':4 ,'name':'arian','age':21,'name':'arian'} 
print(x2)

x3={'age':21, 'roll':4 ,'name':'arian','age':23} 
print(x3)

#Python allows duplicate keys while creating a dictionary literal.
#The last occurrence of the key is kept.

x4={'age':21, 'roll':4 ,'name':'arian'} 
print(x4.pop('age')) #pop()...
print(x4)

print(x4.get('regno','not avail')) #if keys not avail in the dict


print(x4.keys()) #print all keys
print(x4.values())
print(x4.items())


x4['age']=30 #modification
print(x4)

#for loop

for key,values in x4.items():
    print(key,values,sep='_')

x4.clear() #clear() full dict
print(x4)