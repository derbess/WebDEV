def first_last6(nums):
  return nums[0]==6 or nums[-1]==6
def same_first_last(nums):
  return len(nums)>=1 and nums[0]==nums[-1]
def common_end(a, b):
  return a[0] == b[0] or a[-1] == b[-1]
def sum3(nums):
  return sum(nums)
def rotate_left3(nums):
  return nums[1:] + nums[0:1]
def reverse3(nums):
  return nums[::-1]
def max_end3(nums):
  return [max(nums[0],nums[-1])]*3
def sum2(nums):
def middle_way(a, b):
  return [a[1],b[1]]
def make_ends(nums):
  return [nums[0],nums[-1]]
def has23(nums):
  return nums[0]==2 or nums[1]==3 or nums[0]==3 or nums[1]==2
