from heapq import heapify, heappop
import math
n = input()
locs = []
for i in range(n):
	ls = raw_input().split(' ')
	locs.append((int(ls[2]),(int(ls[0]), int(ls[1]))))
m = input()
heapify(locs)
path = []
traveled = 0
currentPos = (0, 0)
for i in xrange(len(locs)):
	time, xy = heappop(locs)
	distance = math.sqrt((currentPos[0] - xy[0])**2 + (currentPos[1] - xy[1])**2) + traveled
	currentPos = xy
	traveled += distance
	path.append((distance, time))
dontStop = True
i = 0
counter = 0
ic = 0
n = len(path)
while dontStop:
	i += .001
	for item in path:
		if ic == 0 and item[1] * i >= item[0]:
			counter += 1
		else:
			if item[1] * i * (m ** ic) >= item[0]:
				counter += 1
		ic += 1
	if counter == n:
		break
	counter = 0
	ic = 0
print i







# G = []
# currentPos = (0, 0)
# currentTime = 0
# previous = -1
# while locs:
# 	time, xy = heappop(locs)
# 	distance = math.sqrt((currentPos[0] - xy[0])**2 + (currentPos[1] - xy[1])**2)
# 	currentPos = xy
# 	velocity = distance / (time - currentTime)
# 	G.append([velocity, (distance, xy, time)])
# 	if previous >= 0:
# 		if (velocity / m) * G[previous][1][2] >= G[previous][1][0]:
# 			G[previous][0] = velocity / m
# 		else:
# 			G[previous + 1][0] = (G[previous][0] * m)
# 	previous += 1
# 	currentTime += time
# print G[0][0]