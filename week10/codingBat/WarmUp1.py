def sleep_in(weekday, vacation):
  if not weekday and not vacation:
    return True
  elif weekday and not vacation:
    return False
  elif not weekday and vacation:
    return True
  else:
    return True


def monkey_trouble(a_smile, b_smile):
  return a_smile==b_smile

def sum_double(a, b):
  c = a+b
  if a==b:
    return c*2
  return c

def diff21(n):
  if n>21:
    return (n-21)*2
  return 21-n

def parrot_trouble(talking, hour):
  return talking and (hour not in range(7,21))

def makes10(a, b):
  return a==10 or b==10 or a+b==10

def near_hundred(n):
  return n in range(90,111) or n in range(190,211)

def pos_neg(a, b, negative):
  if not negative:
    return (a>0 and b<0) or (a<0 and b>0)
  else:
    return a<0 and b<0
def not_string(str):
  if len(str)>2 and str[0]=='n' and str[1]=='o' and str[2]=='t':
    return str
  return "not "+ str

def missing_char(str, n):
  return str[:n] + str[n+1:]
  
def front_back(str):

	if len(str) == 1 or len(str) == 0:
		return str

	if len(str) == 2:
		return str[::-1]

	return str[-1] + str[1:-1] + str[0]

def front3(str):
  if len(str)>=3:
    return str[0:3] + str[0:3] + str[0:3]
  else:
    return str[0:] + str[0:] + str[0:]
