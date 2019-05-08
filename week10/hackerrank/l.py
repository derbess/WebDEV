# Tuples
T = ()

def main():
	N = int(input())
	
	T = tuple([int(x) for x in input().split()])

	print(hash(T))
	
	
if __name__ == '__main__':
	main()