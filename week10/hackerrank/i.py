# Python: Nested Lists
D = {}
M = -1

def main():	
	for _ in range(int(input())):
		name = input()
		score = float(input())

		D[name] = score

	mini = min(D.values())

	for el in sorted(D.values()):
		if el != mini:
			M = el

			break

	for namee in sorted(D):
		if D[namee] == M:
			print(namee)


	
if __name__ == '__main__':
	main()