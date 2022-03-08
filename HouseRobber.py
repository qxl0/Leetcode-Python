nums = [1,2,3,1]

def hosueRobber(nums):
  dp = [0 for i in range(len(nums)+1)]
  dp[0] = 0
  dp[1] = nums[0]
  for i in range(2,len(nums)+1):
    dp[i] = max(dp[i-1], dp[i-2]+nums[i-1])
  return dp[len(nums)]


if __name__ == '__main__':
  res = hosueRobber(nums)
  print("result is: ", res)