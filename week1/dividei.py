try:
	a=input("enter value of a:")
	b=input("enter value of b:")
	div=float(a)/float(b)
	print("the result=",div)
except ValueError:
	print("enter either integer or float")
