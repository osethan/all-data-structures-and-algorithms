
def can_jump(nums):
  """
  Given an array of non-negative integers, you are initially positioned at the first index of the array.
  Each element in the array represents your maximum jump length at that position.
  Determine if you are able to reach the last index.
  For example:
  A = [2,3,1,1,4], return true.
  A = [3,2,1,0,4], return false.
  """
  def jump(nums, pos):
    if pos == len(nums)-1:
      return True
    step = nums[pos]
    while step > 0:
      new_pos = pos + step
      if jump(nums, new_pos):
        return True
      step -= 1
    return False
  return jump(nums, 0)