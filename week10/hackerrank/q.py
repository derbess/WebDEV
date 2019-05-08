# Find a string

def count_substring(string, sub_string):
	s_size = len(string)
	ss_size = len(sub_string)

	return sum([1 for i in range(s_size - ss_size + 1) if string[i:i+ss_size] == sub_string])

def main():
	a = input()
	b = input()
	
	print(count_substring(a, b))
	
if __name__ == '__main__':
	main()