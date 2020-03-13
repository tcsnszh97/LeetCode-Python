# 0169.多数元素

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        l = len(nums)
        for val in nums:
            if val not in dic:
                dic[val] = 1
            else:
                dic[val] += 1
            if dic[val]>(l/2):
                    return val
```
