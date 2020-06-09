
def three_sum(nums):
  def twoSum(nums, i, seen):
    ilo, ihi = i+1, len(nums)-1
    while ilo < ihi:
      nsum = nums[ilo] + nums[ihi]
      if nsum == -nums[i]:
        seen.append([nums[i], nums[ilo], nums[ihi]])
        ilo += 1
        while nums[ilo] == nums[ilo-1]: ilo += 1
        ihi -= 1
        while nums[ihi] == nums[ihi+1]: ihi -= 1
      elif nsum < -nums[i]:
        ilo += 1
        while nums[ilo] == nums[ilo-1]: ilo += 1
      else:
        ihi -= 1
        while nums[ihi] == nums[ihi+1]: ihi -= 1
    return seen
  
  nums.sort()
  seen = []
  for i in range(len(nums)-2):
    seen += twoSum(nums, i, [])
  return seen

def three_sum_slow(nums):
  nums.sort()
  seen = set()
  for i in range(len(nums)-2):
    for j in range(i+1, len(nums)-1):
      for k in range(j+1, len(nums)):
        if nums[i] + nums[j] + nums[k] == 0:
          seen.add(str([nums[i], nums[j], nums[k]]))
  return [[int(d) for d in s.strip('[]').split(', ')] for s in seen]
