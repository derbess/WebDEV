def double_char(str):
  return ''.join([i*2 for i in str])
def count_hi(str):
  return sum([1 for i in range(len(str)-1) if str[i:i+2] == 'hi'])
def cat_dog(str):
  return sum([1 for i in range(len(str)-2) if str[i:i+3] == 'cat'])==sum([1 for i in range(len(str)-2) if str[i:i+3] == 'dog'])

def count_code(str):
	return sum([1 for i in range(len(str)-3) if str[i:i+2] == 'co' and str[i+3] == 'e'])

def end_other(a, b):
	return a[-len(b):].lower() == b[-len(a):].lower()

def xyz_there(str):
	return sum([1 for i in range(1, len('#' + str)-2) if ('#'+str)[i:i+3] == 'xyz' and ('#'+str)[i-1] != '.']) > 0