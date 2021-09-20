
a=int(input("Add your first number in list " ))
b=int(input("Add your second number in list " ))
c=int(input("Add your third number in list " ))
d=int(input("Add your fourth number in list " ))
e=int(input("Add your fifth number in list " ))

list1 = [a,b,c,d,e]
  
generic_comp =  (i for i in list1 if 2* i)
  
print ("Generic comprehensions: " +str(generic_comp))