# Lists
L = []

def main():
	N = int(input())
	
	for _ in range(N):
		query = input()

		if 'insert' in query:
			nums = query.split()[1:]

			L.insert(int(nums[0]), int(nums[1]))

		elif query == 'print':
			print(L)

		elif 'remove' in query:
			L.remove(int(query.split()[1]))

		elif 'append' in query:
			L.append(int(query.split()[1]))

		elif query == 'sort':
			L.sort()

		elif query == 'pop':
			L.pop()

		elif query == 'reverse':
			L.reverse()

if __name__ == '__main__':
	main()