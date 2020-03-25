# 三维形体的表面积

```python
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        l = len(grid)
        w = len(grid[0])
        res = 0
        for i in range(l):
            for j in range(w):
                # 计算前后左右表面积

                # 前表面积
                if i == l-1:
                    res += grid[i][j]
                else:
                    dif = grid[i][j] - grid[i+1][j]
                    if dif > 0:
                        res += dif
                # 后表面积
                if i == 0:
                    res += grid[i][j]
                else:
                    dif = grid[i][j] - grid[i-1][j]
                    if dif > 0:
                        res += dif
                # 左表面积
                if j == 0:
                    res += grid[i][j]
                else:
                    dif = grid[i][j] - grid[i][j-1]
                    if dif > 0:
                        res += dif
                # 右表面积
                if j == w-1:
                    res += grid[i][j]
                else:
                    dif = grid[i][j] - grid[i][j+1]
                    if dif > 0:
                        res += dif
                # 上下表面积
                if grid[i][j] != 0:
                    res += 2
        return res
```
