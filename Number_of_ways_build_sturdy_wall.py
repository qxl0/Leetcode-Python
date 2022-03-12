class Solution:
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

if __name__ == '__main__':
  s = Solution()
  height = 3
  width = 4
  bricks = [1,2]
  s.BuildWall(height,width, bricks)