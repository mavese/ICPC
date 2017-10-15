def cashiersAlg(S, cntr):
	i = 0
	ncoins = 0
	while i < cntr:
		for n in range(len(S)):
			if S[(len(S)-1) - n] + i <= cntr:
				i += S[(len(S)-1) - n]
				ncoins += 1
				break
	return ncoins

if __name__ == '__main__':
	for i in range(10):
		n = input()
		S = list(input())

		if n <= 1:
			print("canonical")

		smllstCntr = (S[len(S)-2] + S[len(S)-1]) - 1
		if cashiersAlg(S, smllstCntr) < cashiersAlg(S[:len(S)-1], smllstCntr):
			print "canonical"
		else:
			print "non-canonical"