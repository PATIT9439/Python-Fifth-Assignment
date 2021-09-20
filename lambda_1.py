a=int(input("Add your first number in list " ))
b=int(input("Add your second number in list " ))
c=int(input("Add your third number in list " ))
d=int(input("Add your fourth number in list " ))
e=int(input("Add your fifth number in list " ))

list1 = [a,b,c,d,e]

even = list(filter(lambda x: x%2 == 0, list1))
print(f"Number of even numbers in the above array: {even}")
odd = list(filter(lambda x: x%2 != 0, list1))
print(f"Number of even numbers in the above array: {odd}")
