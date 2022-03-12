# nums = [1,2,3,1]
# nums = [183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]
nums = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
def houseRobber(nums):
  dp = [0 for i in range(len(nums)+1)]
  dp[0] = 0
  dp[1] = nums[0]
  for i in range(2,len(nums)+1):
    dp[i] = max(dp[i-1], dp[i-2]+nums[i-1])
  return dp[len(nums)]


#Recursive
def houseRobber_Recursive(nums):
  return houseRobber_Recursive_helper(len(nums)-1)

def houseRobber_Recursive_helper(index):
  if index == 0:
    return nums[0]
  if index < 0:
    return 0
  pickIndex = nums[index] + houseRobber_Recursive_helper(index - 2)
  notPickIndex = houseRobber_Recursive_helper(index - 1)
  return max(pickIndex, notPickIndex)

#Memorization
# dp = [-1 for i in range(len(nums))]
dp = [-1] * len(nums)

def houseRobber_Mem(nums):
  return houseRobber_Mem_helper(len(nums)-1)

def houseRobber_Mem_helper(index):
  if index == 0:
    return nums[0]
  if index < 0:
    return 0
  if dp[index] > 0:
    return dp[index]

  pickIndex = nums[index] + houseRobber_Recursive_helper(index - 2)
  notPickIndex = houseRobber_Recursive_helper(index - 1)
  dp[index] = max(pickIndex, notPickIndex)
  return dp[index]


if __name__ == '__main__':
  # res = houseRobber_Mem(nums)
  res = houseRobber(nums)
  print("result is: ", res)
# nums = [1,2,3,1]
nums = [
    183,
    219,
    57,
    193,
    94,
    233,
    202,
    154,
    65,
    240,
    97,
    234,
    100,
    249,
    186,
    66,
    90,
    238,
    168,
    128,
    177,
    235,
    50,
    81,
    185,
    165,
    217,
    207,
    88,
    80,
    112,
    78,
    135,
    62,
    228,
    247,
    211,
]
# nums = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
def houseRobber(nums):
    dp = [0 for i in range(len(nums) + 1)]
    dp[0] = 0
    dp[1] = nums[0]
    for i in range(2, len(nums) + 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])
    return dp[len(nums)]


# Recursive
def houseRobber_Recursive(nums):
    return houseRobber_Recursive_helper(len(nums) - 1)


def houseRobber_Recursive_helper(index):
    if index == 0:
        return nums[0]
    if index < 0:
        return 0
    pickIndex = nums[index] + houseRobber_Recursive_helper(index - 2)
    notPickIndex = houseRobber_Recursive_helper(index - 1)
    return max(pickIndex, notPickIndex)


# Memorization
# dp = [-1 for i in range(len(nums))]
dp = [-1] * len(nums)


def houseRobber_Mem(nums):
    return houseRobber_Mem_helper(len(nums) - 1)


def houseRobber_Mem_helper(index):
    if index == 0:
        return nums[0]
    if index < 0:
        return 0
    if dp[index] > 0:
        return dp[index]

    pickIndex = nums[index] + houseRobber_Recursive_helper(index - 2)
    notPickIndex = houseRobber_Recursive_helper(index - 1)
    dp[index] = max(pickIndex, notPickIndex)
    return dp[index]


if __name__ == "__main__":
    # res = houseRobber_Mem(nums)
    res = houseRobber(nums)
    print("result is: ", res)
