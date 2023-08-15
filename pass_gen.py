from random import choice, randint

def passw_gen(passw_len = 12, passw_syms = False):
	passw_alphabet = '0123456789ABCDEFGHIJKLMOPQRSTUVWXYZ'
	passw_syms = '!@#$%^&*()-_=+/?|'

	return(''.join([str(choice(passw_alphabet).lower() if randint(0, 1) else choice(passw_alphabet)) if not passw_syms else choice(passw_syms) if randint(0, 1) else str(choice(passw_alphabet).lower() if randint(0, 1) else choice(passw_alphabet)) for counter in range(passw_len)]))

print(passw_gen(passw_syms=False))