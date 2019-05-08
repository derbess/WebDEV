# String Split and Join

def split_and_join(line):
    return '-'.join(line.split())

def main():
	print(split_and_join(input()))

if __name__ == '__main__':
	main()