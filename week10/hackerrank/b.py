# Python If-Else
Y = 'Wierd'
N = 'Not Weird'

def main():
	n = int(input())

	if n % 2 == 0:
		if n in range(2, 6):
			print(N)

		elif n in range(6, 21):
			print(Y)

		elif n > 20:
			print(N)

	else:
		print(Y)
	
if __name__ == '__main__':
	main()