def factorial(a):
	temp=1
	for i in xrange(1,a,1):
		temp*=i+1
	return temp

def fibonacci(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a


