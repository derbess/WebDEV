# String Validators
N = 5

def main():
	line = input()
	
	D = [False for _ in range(N)]

	for ch in line:
		if ch.isalnum():
			D[0] = True
		
		if ch.isalpha():
			D[1] = True

		if ch.isdigit():
			D[2] = True

		if ch.islower():
			D[3] = True

		if ch.isupper():
			D[4] = True

	for el in D:
		print(el)

if __name__ == '__main__':
	main()