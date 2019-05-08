def cigar_party(cigars, is_weekend):
  return ((cigars>=40 and cigars<=60) and not is_weekend) or (is_weekend and cigars >= 40)
def date_fashion(you, date):
  
  if you<=2 or date<=2:
    return 0
  elif you>=8 or date>=8:
    return 2
  else:
    return 1
def squirrel_play(temp, is_summer):
	return (is_summer and temp in range(60, 101)) or (not is_summer and temp in range(60, 91))

def caught_speeding(speed, is_birthday):
	j = 0

	if is_birthday:
		j = 5

	if speed <= 60 + j:
		return 0
	elif speed in range(61 + j, 81 + j):
		return 1
	else:
		return 2


def sorta_sum(a, b):
	if a+b in range(10, 20):
		return 20

	return a+b

def alarm_clock(day, vacation):
	if vacation:
		if day in (0, 6):
			return 'off'
		else:
			return '10:00'
	else:
		if day in (0, 6):
			return '10:00'
		else:
			return '7:00'

def love6(a, b):
	return a == 6 or b == 6 or a + b == 6 or abs(a-b) == 6

def in1to10(n, outside_mode):
	return (outside_mode and n not in range(2, 10)) or (not outside_mode and n in range(1, 11))

def near_ten(num):
	return num % 10 in (0, 1, 2, 8, 9)