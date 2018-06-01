prev = 1
next = 1
i = 0
sum = 0

while i < 4000000:
	if i % 2 == 0:
		sum += i
	i = prev + next
	prev = next
	next = i


print(sum)
