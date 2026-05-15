a=10
print(a)
print(type(a))

a=12+3j
print(a)
print(type(a))

a=True
print(a)
print(type(a))


#python list..

a=[10,'arian',67.5] #allow duplicate value
print(a)
print(type(a))

#python tuple..

a=(10,'arian',67.5) #allow
print(a)
print(type(a))

#python set...

a={10,'arian',67.3} #donot allow
print(a)
print(type(a))

#python dict.... (key+value)

a={'age':21} #key must be unique , (same key-value diff) print new value , (same key, same value) donot allow duplicate key print only one 
print(a)
print(type(a))
print(a.get('age')) #use get() to access key value 

a={'age':21 , 'age':31}
print(a)