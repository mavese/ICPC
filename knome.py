n = input()
listOfGroups = []
for i in xrange(n):
	ls = raw_input().split(' ')
	results = map(int, ls[1:])
	listOfGroups.append(results)
for lst in listOfGroups:
	counter = 1
	while True:
		if lst[counter] != lst[counter - 1] + 1: break
		counter	+= 1
	print counter + 1