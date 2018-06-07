
"""Run with script

python3 Problem7.py [number]

"""

import sys
import time
import math

def getFactorial(num):
	factors = []
	for i in range(1, math.ceil(math.sqrt(num + 1))):
		if num % i == 0:
			factors.append(i)
	return factors


t0 = time.time()
i = 0
count = 0

while count != int(sys.argv[1]) + 1:
	i += 1
	if len(getFactorial(i)) <= 1:
		count += 1
	

print("The solution is " + str(i))
t1 = time.time()
  
# Added timer due to brute force aspect of the problem being slow
print("This took %.3f seconds to solve" % (t1-t0))


