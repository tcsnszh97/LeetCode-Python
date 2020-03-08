from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.findKthLargestHelper(0, len(nums)-1, nums, k)
    
    def findKthLargestHelper(self, first, last, nums: List[int], k: int) -> int:
        basicvalue = nums[first]
        leftmark = first + 1
        rightmark = last
        while leftmark <= rightmark:
            while leftmark <= rightmark and nums[leftmark] <= basicvalue:
                leftmark += 1
            while leftmark <= rightmark and basicvalue < nums[rightmark]:
                rightmark -= 1
            if leftmark < rightmark:
                nums[leftmark],nums[rightmark] = nums[rightmark],nums[leftmark]
        nums[rightmark],nums[first] = nums[first],nums[rightmark]
        if rightmark == len(nums)-k:
            return nums[rightmark]
        elif rightmark > len(nums)-k:
            return self.findKthLargestHelper(first, rightmark-1, nums, k)
        else:
            return self.findKthLargestHelper(rightmark+1, last, nums, k)