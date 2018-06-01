"""Run with script

python3 Problem3.py [number]

Instead of using a faster method that involved parsing known prime numbers, this script will find the largest prime factor of 
any integer entered. It also outputs time taken to run the computation as for larger numbers it will be incredibly slow"""

import sys
import time

# Note this does not use recursion (ultimately more efficient) due to python limitations
def checkPrime(factors):
	primes = []
	for num in factors:
		newFactors = getFactorial(num)
		if len(newFactors) <= 2:
			primes.append(num)

	return primes


def getFactorial(num):
	factors = []
	for i in range(1, num + 1):
		if num % i == 0:
			factors.append(i)
	return factors

def main():
	t0 = time.time()
	factors = getFactorial(int(sys.argv[1]))
	primes = checkPrime(factors)
	print("The solution is " + str(max(primes)))
	t1 = time.time()
  
  # Added timer due to brute force aspect of the problem being slow
	print("This took %.3f seconds to solve" % (t1-t0))

main()
