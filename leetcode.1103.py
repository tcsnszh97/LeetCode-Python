from typing import List
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        leftover = candies
        ans = [0]*num_people
        num = 1
        index = 0

        while leftover:
            if leftover > num:
                ans[index] += num
                leftover -= num
                num += 1
            else:
                ans[index] += leftover
                leftover -= leftover

            if (index+1)%num_people == 0:
                index = 0
            else:
                index += 1
        return ans