from random import choice, randint

# def passw_gen(passw_len = 12, passw_syms = False):
# 	passw_alphabet = '0123456789ABCDEFGHIJKLMOPQRSTUVWXYZ'
# 	passw_syms = '!@#$%^&*()-_=+/?|'

# 	return(''.join([str(choice(passw_alphabet).lower() if randint(0, 1) else choice(passw_alphabet)) if not passw_syms else choice(passw_syms) if randint(0, 1) else str(choice(passw_alphabet).lower() if randint(0, 1) else choice(passw_alphabet)) for counter in range(passw_len)]))

# print(passw_gen(passw_syms=False))


def passw_gen(passw_len = 12, passwords_to_gen : int = 1, use_letters : bool = True, use_numbers : bool = True, use_symbols : bool = True, letters_random_case : bool = True, add_separator_every_n_syms : int = 0, separator_symbol : str = '-') -> list[str]:
	integers = '0123456789' 
	letters = 'ABCDEFGHIJKLMOPQRSTUVWXYZ'
	symbols = '!@#$%^&*()-_=+/?|'


	alphabet_params = {'use_nums' : use_numbers, 'use_lets' : use_letters, 'use_syms' : use_symbols}
	alphabet_params = {key : alphabet_params[key] for key in alphabet_params if alphabet_params[key]}

	output = []

	for password_number in range(passwords_to_gen):
		password = ''

		for symbol_counter in range(passw_len):
			match choice(list(alphabet_params.keys())):
				case 'use_nums':
					password += choice(integers)
				
				case 'use_lets':
					password += choice(letters) if randint(0, 1) or not letters_random_case else choice(letters).lower()
				
				case 'use_syms':
					password += choice(symbols)

			# print(passw_len, symbol_counter, passw_len % (symbol_counter + 1))

			if add_separator_every_n_syms and not ((symbol_counter + 1) % add_separator_every_n_syms) and symbol_counter and symbol_counter != passw_len - 1:
				# print(symbol_counter, add_separator_every_n_syms - 1)
				password += separator_symbol
			
			elif add_separator_every_n_syms == 1:
				password += separator_symbol
			
		output.append(password)
	
	return(output)

print(passw_gen(16, 20, use_symbols=False, letters_random_case = False, add_separator_every_n_syms=4))