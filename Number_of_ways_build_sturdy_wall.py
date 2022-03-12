from re import M


class Solution:
  M = 1e9+7
  def BuildWall(self, height, width, bricks):
    bricksSet = set(bricks)
    plans = []

    m = width -1 
    for state in range(1<<m):
      # for any state, 
      # state = 2, width = 4
      #  0 1 0 
      # x x x x
      # [-1, 2, 4]
      # brick width validation :
      # 1st: 
      temp = [-1]
      for i in range(m):
        if (state>>i)&1:
          temp.append(i)
      temp.append(m)
      flag = 1
      for i in range(1, len(temp)):
        if temp[i]-temp[i-1] not in bricksSet:
          flag = 0
          break
      if flag:
        plans.append(state)
    print("all plans", plans)

    # dp
    dp = [ [0 for j in range(len(plans))] for i in range(height) ]
    dp[0] = [1] * len(plans) 
    for i in range(1, height):
      for j in range(len(plans)):
        # dp[i][j]
        for k in range(len(plans)):
          if plans[j] & plans[k] == 0:
            dp[i][j] = (dp[i][j] + dp[i-1][k]) % M
    ret = 0
    for p in range(len(plans)):
      ret = (ret + dp[height-1][p]) % M
    return ret

if __name__ == '__main__':
  s = Solution()
  height = 1
  width = 1
  bricks = [2]
  res = s.BuildWall(height,width, bricks)
  print("total number of plans to build is: ", res)