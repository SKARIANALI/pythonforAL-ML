num = int(input("Enter a number: "))
for i in range(1, 11):
 print(num, "*", i, "=", num * i)
 
password = "learncoding123"
a= input("Enter password: ")
while password != a:
 a = input("Enter password again: ")
else:
    print("Congratulation, Unlocked")