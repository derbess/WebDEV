# Python: Find the Runner-Up Score!

def main():
	a = int(input())
	
	arr = [int(x) for x in input().split()]

	maxi = max(arr)

	for el in sorted(arr)[::-1]:
		if el != maxi:
			print(el)

			break
	
if __name__ == '__main__':
	main()