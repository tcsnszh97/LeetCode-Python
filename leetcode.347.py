from typing import List
import collections
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        print(count.get)
        return heapq.nlargest(k, count.keys(), key=count.get) 