'''nums = list('5 3 1')
space_1 = nums.index(' ')
nums.reverse()
space_2 = nums.index(' ')
nums.reverse()
a_num = int(''.join((nums[ : space_1])))
b_num = int(''.join((nums[ space_1+1 : -space_2])))
n_num = int(''.join((nums[-space_2 : ]))) 

print('YES' if (a_num-b_num)%2 == 0 and (a_num-b_num) >= 2*n_num else 'NO')'''


n_num = 3
m_num = 7
buckets_count = 0
prime_nums = [2,3,5,7,11,13,17,19,23]

first_square = n_num**2 if n_num<m_num else m_num**2
main_square = n_num*m_num

def find_square(number, minimal, middle_count = 0, counter = 0):
	while middle_count!=number:
		counter+=1
		middle_count = counter**2
		if counter == 100:
			counter = 'No'
			break
	return(counter)

def multuppling(list_, out = 1):
	for elem in list_:
		out*=elem
	return(out)

while main_square!=0:
	if buckets_count == 0:
		print("Общая площадь", main_square)
		main_square-=first_square
		print("Вычли первый квадрат", main_square)

	else:
		mult = find_square(main_square, n_num if n_num<m_num else m_num)
		print(main_square, mult)
		if mult == 'No':
			square_dec = main_square
			decs = []
			while square_dec!=1:
				for number in prime_nums:
					if square_dec%number==0:
						decs.append(number)
						square_dec/=number

			if len(decs)==1:
				decs.append(1)
				n=decs[0]
				m=decs[1]

			elif len(decs) == 2:
				n=decs[0]
				m=decs[1]

			else:
				middle = len(decs)//2
				n = multuppling(decs[ : middle])
				m = multuppling(decs[ middle : ])

			mult = find_square(n*m)

			if mult!='No':
				main_square=n*m - mult**2

			else:
				main_square-= n**2 if n<m else m**2

		else:
			main_square-=mult**2
			print('Вычли квадрат', main_square, mult)

	buckets_count+=1

print(buckets_count)