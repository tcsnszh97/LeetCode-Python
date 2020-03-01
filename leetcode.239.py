from collections import deque
from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n*k == 0:
            return []
        if k == 1:
            return nums
        
        def insert_deque(i):
            print(deq,"1")
            if deq and deq[0] == i-k:
                deq.pop()
            print(deq,"2")
            while deq and nums[deq[-1]] < nums[i]:
                deq.popleft()
            deq.append(i)

        deq = deque()
        for i in range(k):
            insert_deque(i)
        max_list = [nums[deq[0]]]

        for i in range(k,n):
            print(deq)
            insert_deque(i)
            print(deq)
            max_list.append(nums[deq[0]])

        return max_list

S = Solution()
test = [7,2,4]
k = 2
print(S.maxSlidingWindow(test, k))