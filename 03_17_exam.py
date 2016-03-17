def isPrime(N):
	prime=1
	for x in range(2,N):
		if (N%x==0):
			prime=0
	return prime

sum=0
for x in range(2,1000):
	if(isPrime(x)==1):
		sum+=x
print sum