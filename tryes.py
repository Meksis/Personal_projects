x=1111
x4=int(x)
kol_raz=0
while x4>=1:
	kol_raz+=1
	x4 = x4//10
	print(x4)
if kol_raz%2==0:
	print('четное')
else:
	print('нечетное')