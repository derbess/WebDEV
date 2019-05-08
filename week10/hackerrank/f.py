# Python: Print Function

def main():
	a = int(input())
	
	for i in range(a):
		print(str(i+1), end='')

	print()
	
if __name__ == '__main__':
	main()