text1 = "abcde"
text2 = "ace"
m = len(text1)+1
n = len(text2)+1
dp = [[0 for j in range(n)] for i in range(m)]
# dp=[[0 for j in range(len(text2+1))] for i in range(len(text1)+1)]

for i in range(m -2, -1, -1):
  for j in range(n-2, -1, -1):
    if text1[i] == text2[j]:
      dp[i][j] = 1 + dp[i+1][j+1]
    else:
      dp[i][j] = max(dp[i][j+1], dp[i+1][j])
print("result is:", dp[0][0])