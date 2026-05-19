# Exception Handling Example in Python

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    
    c = a / b
    
    print("Result:", c)

except Exception:
    print("Can not divide by 0")

else:
    print("Ankit") #else runs only when no error occurs.



try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b

    print("Result =", result)

except ZeroDivisionError:
    print("You cannot divide by zero!")

except ValueError:
    print("Please enter only numbers!")

finally:
    print("Program finished")
    
    
'''try → Code that may create an error
   except → Handles the error
   finally → Always runs whether error happens or not'''