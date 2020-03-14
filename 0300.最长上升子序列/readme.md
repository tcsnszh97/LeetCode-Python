# 0300.最长上升子序列

## 解题思路

当题目的问题可以分成许多子问题，并且子问题有许多重叠的求解部分，就满足了用动态规划来求解的条件。

求解动态规划问题，最重要的是弄清楚两点。

1. 确定dp数组存放什么数据。

2. 假设已经解决前n-1个子问题，如何解决第n个问题。

### 方法1 动态规划

使用一个dp数组，dp[x]的值表示一定取nums[x]作为子序列最后一个值时，该子序列的最长长度。

如[1,3,4,2]，dp[3]则为取nums[3]作为结尾即子序列[1,2]的长度，即2。当然，这个子序列并不一定是唯一的。

那么如何解决第n个问题，只需要遍历dp数组，如果nums[i]的值比nums[n]小，那么意味着可以将nums[n]插入该序列，那么子序列长度就为dp[i]+1，计算出所有子序列的长度，得到的最大值就为dp[n]的值。

最后再遍历dp数组，最大值即为nums数组最长上升子序列的长度。

```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        dp = [0]*len(nums)
        dp[0] = 1
        for i in range(1, len(nums)):
            maxlen = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    maxlen = max(maxlen, dp[j]+1)
            dp[i] = maxlen
        return max(dp)
```

该注意的点，dp[0]的值为1，若只有一个值则最长子序列长度为1。
