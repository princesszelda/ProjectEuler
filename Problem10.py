a = []
maxV = 2000000

for i in range (maxV + 1):
	a.append(True)

count = 2

while count * count <= maxV:
	if a[count] == True:
		for j in range(count *2, maxV + 1, count):
			a[j] = False
	count += 1

total = 0
for k in range (2, maxV):
	if a[k]:
		total += k

print(total)