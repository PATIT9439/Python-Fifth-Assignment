
def power(a, b):

	if b == 0:
		return 1
	
	elif b == 1:
		return a
	
	else:
		return (a*power(a, b-1))

a = int(input("Enter the number :"))
b = int(input("Enter power :"))

print(power(a, b))

