def count_evens(nums):
	return sum([1 for num in nums if num % 2 == 0])

def big_diff(nums):
	return max(nums) - min(nums)

def centered_average(nums):
	return sum(sorted(nums)[1:-1]) // (len(nums)-2)

def sum13(nums):
	res, i = 0, 0

	while i < len(nums):
		if nums[i] == 13:
			i += 2
		else:
			res += nums[i]
			i += 1

	return res

def sum67(nums):
	res, i, Q = 0, 0, False

	while i < len(nums):
		if nums[i] == 6:
			Q = True
		elif nums[i] == 7:
			if Q:
				Q = False
			else:
				res += nums[i]
		elif not Q:
			res += nums[i]

		i += 1

	return res

def has22(nums):
	return sum([1 for i in range(len(nums)) if nums[i:i+2] == [2, 2]]) > 0

def xyz_there(str):
	return sum([1 for i in range(1, len('#' + str)-2) if ('#'+str)[i:i+3] == 'xyz' and ('#'+str)[i-1] != '.']) > 0