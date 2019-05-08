# Mutations

def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]

def main():
	string = input()
	data = input().split()

	print(mutate_string(string, int(data[0]), data[1]))

if __name__ == '__main__':
	main()