# sWAP cASE

def swap_case(s):
	res = ''

	for ch in s:
		if ch.islower():
			res += ch.upper()

		else:
			res += ch.lower()

	return res

def main():
	line = input()

	print(swap_case(line))

if __name__ == '__main__':
	main()