def string_times(str, n):
  return str*n

def front_times(str, n):
  if len(str)>=3:
    return str[0:3]*n
  else:
    return str[0:]*n

def string_bits(str):
  return str[0::2]

def string_splosion(str):
  st=""
  for i in range (len(str)):
    st+=str[0:i+1]
  return st

def last2(str):
  cnt = 0
  for i in range(len(str)-2):
    if str[i:i+2] == str[-2:]:
      cnt+=1
  return cnt

def array_count9(nums):
  cnt =0
  for i in range (len(nums)):
    if nums[i]==9:
      cnt+=1
  return cnt
  
def array_front9(nums):
  return 9 in nums[0:4]

def array123(nums):
  for i in range(len(nums)-2):
    if nums[i] == 1 and nums[i+1]==2 and nums[i+2] == 3:
      return True
  return False

def string_match(a, b):
  cnt =0
  ans =0
  for i in range(min(len(a)-1,len(b)-1)):
    if a[i] == b[i] and a[i+1] == b[i+1]:
      cnt+=1
  return cnt
