class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        leftsymbol = ['(','{','[']
        rightsymbol = [')','}',']']
        for symbol in s:
            if symbol in leftsymbol:
                stack.append(symbol)
            elif symbol in rightsymbol:
                index = rightsymbol.index(symbol)
                if not stack:
                    return False
                match = stack.pop()
                if match != leftsymbol[index]:
                    return False
        if stack:
            return False
        return True

test = "()"
c = Solution()
print(c.isValid(test))