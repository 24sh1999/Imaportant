def primes(start, n):
	ps, sieve = [], [True] * (n + 1)
	for p in range(2, n + 1):
		if sieve[p]:
			ps.append(p)
			for i in range(p * p, n + 1, p):
				sieve[i] = False
	startInd = ps.index(start)
	return ps[startInd:]
start = int(input())
n = int(input())
print(primes(start, n))
    
def check(n):
	if n == 1: return False
	for i in range(2, math.floor(math.sqrt(n))):
		if n % i == 0:
			return False
	return True
for i in range(len(a)):
	for j in range(len(a)):
		if i == j:
			continue
		else:
			ps.add(int(repr(a[i]) + repr(a[j])))
