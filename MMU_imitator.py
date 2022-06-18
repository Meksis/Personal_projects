from random import randint

min_number = 2
max_number = 7
allow_duplicates = False


mem_len = (max_number+min_number) // 2


def filler(size, name):
	mem_out = [name]
	for counter in range(size):
		num = bin(randint(min_number, max_number))[3 : ]
		if not allow_duplicates:
			while num in mem_out:
				num = bin(randint(min_number, max_number))[3 : ]
		mem_out.append(num)
	return(mem_out)

mem_1 = filler(mem_len, 1)
mem_2 = filler(mem_len, 2)
mem_3 = filler(mem_len, 3)
mmu_imitator = [mem_1, mem_2, mem_3]

print(mmu_imitator)

action = input('\nType needed action (d+number for deleting mem_number, s for stop) - ')


while True:
	if action[0] == 'd':
		del_num = int(action[1:])
		for mem_num in range(len(mmu_imitator)):
			if mmu_imitator[mem_num][0] == del_num:
				del_num = mmu_imitator[mem_num][0]
				break

		del_mem = filler(mem_len, del_num)

		mmu_imitator.pop(mem_num)
		mmu_imitator.append(del_mem)

		print(f'\nmem_{del_num} has been deleted and replaced succesfully.')
		print(mmu_imitator)

	elif action[0] == 's':
		break
	action = input('\nType needed action (d+number for deleting mem_number, s for stop) - ')