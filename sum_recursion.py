a,b,c,d,e = input("enter nums space seperated").split()

a= int(a)
b = int(b)
c = int(c)
d = int(d)
e = int(e)

num = (a,b,c,d,e)

def recursive_list_sum(data_list):
	total = 0
	for element in data_list:
		if type(element) == type([]):
			total = total + recursive_list_sum(element)
		else:
			total = total + element

	return total
print( recursive_list_sum(num))
