'''import calcu
calcu.calculator(20,10)'''

#From keyword

from calcu import disp 
disp()

from calcu import disp,calculator
disp()
calculator(20,30)

from calcu import * 
calculator(30,50)

#Aliasing with 'as' 

from calcu import disp as display 
display()