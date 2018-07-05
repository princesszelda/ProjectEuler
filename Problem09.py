for a in range(1,500):
	for b in range(250,600):
		for c in range(300, 750):
			if a + b + c == 1000 and a**2 + b**2 == c**2:
				print(a)
				print(b)
				print(c)

print("None")
