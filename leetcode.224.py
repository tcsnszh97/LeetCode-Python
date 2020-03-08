class Solution:
    def calculate(self, s: str) -> int:
        operand = 0
        symbol = 1
        res = 0
        stack = []

        for ch in s:
            if ch.isdigit():
                operand = operand * 10 + int(ch)
            if ch == '+':
                res += (symbol * operand)
                operand = 0
                symbol = 1
            if ch == '-':
                res += (symbol * operand)
                operand = 0
                symbol = -1
            if ch == '(':
                stack.append(res)
                stack.append(symbol)
                res = 0
                symbol = 1
            if ch == ')':
                res += (symbol * operand)
                operand = res
                symbol = stack.pop()
                res = stack.pop()
        return res + (symbol * operand)
            
