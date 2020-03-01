# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         comparedArray = [0]*26
#         for word in s :
#             comparedArray[ord(word)-ord('a')] += 1
#         for word in t :
#             comparedArray[ord(word)-ord('a')] -= 1
#         for i in comparedArray:
#             if i != 0:
#                 return False
#         return True

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic = {}
        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        for j in t:
            if j not in dic:
                return False
            else:
                dic[j] -= 1
        for val in dic.values():
            if val != 0:
                return False
        return True

f = Solution()
s = "anagram"
t = "nagaram"
print(f.isAnagram(s,t))