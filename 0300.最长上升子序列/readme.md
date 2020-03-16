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

时间复杂度O(n^2) 需要遍历数组nums，同时计算dp[i]时又需要遍历dp[0...n-1]

空间复杂度O(n) 用了一个长度为n的数组

该注意的点

1. dp[0]的值为1，若只有一个值则最长子序列长度为1。

2. 对于nums[j] >= nums[i]的情况是不处理的，因为求dp[i]的值只考虑将nums[i]插入子序列结尾的情况。

### 方法2 动态规划+二分查找

新建一个数组lis用来保存最长上升子序列，然后用一个巧妙的方法来计算最长子序列的长度。

假设nums为[1,7,8,2,3,4,5]，遍历到2之前，lis数组先保存了[1,7,8]，此时再将2替换数组中第一个比2大的数，lis变为[1,2,8]。这样做之后有两种情况。

1. [1,7,8]就是最长子序列，虽然lis变成了[1,2,8]，但是len(lis)不变，还是等于3。结果就是之后若找不到比lis更长的子序列，那么也无法改变lis的长度。

2. [1,7,8]并不是最长子序列，如当前假设的nums，不断的将后来遍历到的数替换掉，遍历到nums[4]，lis就会变为[1,2,3]。接着遍历到nums[5]，lis就会更新成[1,2,3,4]，从而巧妙的找到了更长的子序列。

利用这个方法就能在更短的时间复杂度找到最长子序列的长度，而从数组lis中找到第一个大于当前值的位置就用二分查找法就好。最终算法的时间复杂度就在O(nlogn)完成。

```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        lis = []
        for i in range(len(nums)):
            cur_value = nums[i]
            if not lis or lis[-1] < cur_value:
                lis.append(cur_value)
            else:
                left = 0
                right = len(lis) - 1
                middle = left + (right - left) // 2
                if lis[0] >= cur_value:
                    middle = 0
                else:
                    while not (lis[middle - 1] < cur_value and lis[middle] >= cur_value):
                        if lis[middle] > cur_value:
                            right = middle - 1
                            middle = left + (right - left) // 2
                        else:
                            left = middle + 1
                            middle = left + (right - left) // 2
                lis[middle] = cur_value
        return len(lis)
```

该注意的点

1. 写判断条件的时候需要多考虑列表为空或者列表只有一个数的情况下能否满足条件。

2. 二分查找需要仔细的确定判断条件是否包含特殊情况，如判断用大于号还是大于等于号。

3. 题目中找到插入的点有多种情况，需要分开判断。

    第一种情况是lis[0]比cur_value要大，直接替换lis[0]即可。

    第二种情况就是找到一个lis[n] >= cur_value并且lis[n-1] < cur_value。
