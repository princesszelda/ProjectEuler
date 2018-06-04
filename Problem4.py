largest = 998001 # the largest project of two three-digit numbers

'''Finds all three digit factorials of a number'''
def getFactorial3Digit(num):
	factors = []
	for i in range(1, num + 1):
		if num % i == 0 and i >= 100 and i < 1000 and num / i >= 100 and num / i < 1000:
			factors.append(i)
	return factors

'''checks if a number is a palindrome'''
def isPalindrome(num):
	stringNum = str(num)
	revStringNum = stringNum[::-1]
	if stringNum == revStringNum:
		return True
	else:
		return False

'''Will print out all palindromes that are a product of 
two 3-digit numbers, in order of largest first'''
for i in reversed(range(largest)):
	if isPalindrome(i) == True:
		factors = getFactorial3Digit(i)
		if len(factors) == 2:
			print(i)


