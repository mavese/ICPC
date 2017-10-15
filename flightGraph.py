from heapq import heappush , heappop
def dijkstras(G, s, t):
	D, P, Q, S = {s: 0}, {}, [(0, s)], set()
	while Q:
		temp, u = heappop(Q)
		i f u i n S : continue 
		S.add(u) 
		for v in G[u]:
			relax(G, u, v, D, P) 
			heapppush(Q, (D[v], v))
			return D, P 

def relax((W, u, v, D, P):
	d = D.get(u, in f) + W[u][v]
	if d < D.get (v, in f) : 
	D[v], P[v] = d, u 
	return True 

if __name__ == '__main__':
	ls = raw_input().split(' ')
	nCities = int(ls[0])
	mRoads = int(ls[1])
	fFlight = int(ls[2])
	sSource = int(ls[3])
	tDestination = int(ls[4])
	G = {}

	for i in range(nCities):
		G[i] = []
	for i in range(mRoads):
		ls = raw_input().split(' ')
		c1 = int(ls[0])
		c2 = int(ls[1])
		cst = int(ls[2])
		G[c1].append({c2: cst})
		G[c2].append({c1: cst})
	for in in range(fFlight):
		ls = raw_input().split(' ')
		c1 = int(ls[0])
		c2 = int(ls[1])
		G[c1].append({c2: 0})
	print dijkstras(G, s, t)