# Capitalize!

def solve(s):
	res = ''

	for i in range(len(s)):
		if i == 0 and s[i] != ' ':
			res += s[i].upper()

		elif s[i] != ' ' and s[i-1] == ' ':
			res += s[i].upper()

		else:
			res += s[i]

	return res

def main():
	line = input()
	
	print(solve(line))

if __name__ == '__main__':
	main()