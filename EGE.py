print(' A B C D')
for a in range(2):
	for b in range(2):
		for c in range(2):
			for d in range(2):
				if (( a <= d ) and (not(b<=c))) == 1:
					print(a,b,c,d)