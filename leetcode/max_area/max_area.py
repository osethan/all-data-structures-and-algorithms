
def max_area(heights):
  """
  O(N) time, O(1) space
  """
  amax = 0
  ilo, ihi = 0, len(heights)-1
  while ilo < ihi:
    a = (ihi-ilo) * (min(heights[ilo], heights[ihi]))
    amax = max(amax, a)
    if heights[ilo] < heights[ihi]:
      ilo += 1
    else:
      ihi -= 1
  return amax

def max_area_slow(heights):
  """
  O(N2) time, O(1) space
  """
  amax = 0
  n = len(heights)
  for i in range(n-1):
    for j in range(i+1, n):
      a = (j-i) * (min(heights[i], heights[j]))
      amax = max(amax, a)
  return amax