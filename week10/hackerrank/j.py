# Finding the percentage
D = {}
L = 3

def main():
	N = int(input())
	
	for _ in range(N):
		data = input().split()

		D[data[0]] = sum([float(x) for x in data[1:]]) / L

	print("%.2f" % D[input()])
	
if __name__ == '__main__':
	main()