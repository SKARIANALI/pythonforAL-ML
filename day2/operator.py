# 1. Arithmetic Operators

a = 13
b = 2
print(a + b)      # Addition
print(a - b)      # Subtraction
print(a * b)      # Multiplication
print(a / b)      # Division
print(a // b)     # Floor Division
print(a ** b)     # Power



# 2. Relational Operators

print(a < b)      # Less than
print(a > b)      # Greater than
print(a <= b)     # Less than or equal to
print(a >= b)     # Greater than or equal to
print(a == b)     # Equal to
print(a != b)     # Not equal to

# 3. Logical Operators

print(a > b and a < b)
print(a > b or a < b)
print(not (a > b))

# 4. Bitwise Operators

a = 5
b = 6
print(a & b)      # Bitwise AND
print(a | b)      # Bitwise OR
print(a ^ b)      # Bitwise XOR
print(~a)         # Bitwise NOT
print(a >> 1)     # Bitwise Right Shift
print(a << 1)     # Bitwise Left Shift


# 5. Assignment Operators 
a = 5
a += 2            # Equivalent to a = a + 2
print(a)

# 6. Identity Operators 
a = 13
b = 13
print(a is b)     # Checks if both variables point to the same memory ID
print(a is not b) # Checks if they point to different IDs
print(id(a))      # Checking memory address
print(id(b))

# 7. Membership Operators 
text = "India is great"
print("great" in text)    # Check if substring exists
print("hello" not in text) # Check if substring is absent