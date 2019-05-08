# Text Wrap

def wrap(string, max_width):
	return '\n'.join([string[i:i+max_width] for i in range(0, len(string), max_width)])

def main():
	line, w = input(), int(input())
	
	print(wrap(line, w))

if __name__ == '__main__':
	main()