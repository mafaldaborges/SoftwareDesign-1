def check_fermat(a,b,c,n): 
	if n<=2 and a**n + b**n == c**n:
		print "Congrations it worked"
	elif n>2 and a**n + b**n == c**n:
		print "Holy smokes, Fermat was wrong!"
	elif n<=2 and a**n + b**n != c**n:
		print "You failed to find a correct set of numbers"
	elif n>2 and a**n + b**n != c**n:
		print "No, that doesn't work"

def convert_then_fermat(a,b,c,n):	
	a = int(a)
	b = int(b)
	c = int(c)
	n = int(n)
	check_fermat(a,b,c,n)
		