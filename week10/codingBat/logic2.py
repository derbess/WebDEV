def make_bricks(small, big, goal):
	if small + 5*big < goal:
		return False

	if goal // 5 <= big:
		return goal % 5 <= small
	else:
		return goal - 5*big <= small

def lone_sum(a, b, c):
	return sum([x for x in (a, b, c) if [a, b, c].count(x) == 1])

def lucky_sum(a, b, c):
	i = 4

	if 13 in (a, b, c):
		i = [a, b, c].index(13)

	return sum([a, b, c][:i])

def no_teen_sum(a, b, c):
	return sum([fix_teen(x) for x in (a, b, c)])

def fix_teen(n):
	if n in range(13, 20) and n not in (15, 16):
		return 0
	else:
		return n

def round_sum(a, b, c):
	return sum([rround(x) for x in (a, b, c)])

def rround(x):
	if x % 10 >= 5:
		return (x // 10 + 1) * 10
	else:
		return x // 10 * 10

def close_far(a, b, c):
	return (abs(a-b) <= 1 and abs(b-c) >= 2 and abs(a-c) >= 2) or \
			(abs(a-c) <= 1 and abs(a-b) >= 2 and abs(c-b) >= 2)

def make_chocolate(small, big, goal):
	if small + 5*big < goal:
		return -1

	if goal // 5 <= big:
		if goal % 5 <= small:
			return goal % 5
		else:
			return -1
	else:
		if goal - 5*big <= small:
			return goal - 5*big
		else:
			return -1 