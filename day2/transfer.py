if 'coding' in 'learn coding':
 pass # Body to be written later

for num in range(1, 11):
 if num % 2 == 0:
  continue # Skip even numbers
 else:
  print(num)
  
for num in range(1, 11):
 if num % 2 == 0:
  break # Exit the loop entirely
 else:
  print(num) # Only '1' will be printed
