
def three_sum(nums):
  solutions = loopNums(nums)
  return convertSolutions(solutions)


def loopNums(nums):
  solutions = set({})

  for i in range(len(solutions)):
    for j in range(len(solutions)):
      if j == i:
        continue
      for k in range(len(solutions)):
        if k == i or k == j:
          continue
        
        if nums[i] + nums[j] + nums[k] == 0:
          solution = {nums[i], nums[j], nums[k]}
          if solution not in solutions:
            solutions.add(solution)
                      
  return solutions


def convertSolutions(solutions):
  return [list(solution) for solution in solutions]
