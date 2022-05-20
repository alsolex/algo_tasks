class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        for i in range(n):
            for j in range(m):

                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = -1
                    continue

                if i == 0 and j == 0:
                    obstacleGrid[i][j] = 1
                elif i == 0:
                    obstacleGrid[i][j] = obstacleGrid[i][j - 1]
                elif j == 0:
                    obstacleGrid[i][j] = obstacleGrid[i - 1][j]
                else:
                    if obstacleGrid[i - 1][j] == -1 and obstacleGrid[i][j - 1] == -1:
                        obstacleGrid[i][j] == -1
                    elif obstacleGrid[i - 1][j] == -1:
                        obstacleGrid[i][j] = obstacleGrid[i][j - 1]
                    elif obstacleGrid[i][j - 1] == -1:
                        obstacleGrid[i][j] = obstacleGrid[i - 1][j]
                    else:
                        obstacleGrid[i][j] = (
                            obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]
                        )

        return obstacleGrid[-1][-1]
