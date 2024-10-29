class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_paren = {')':'(', '}': '{',']':'['}
        for ch in s:
            if ch in '({[':
                stack.append(ch)
            elif stack and close_paren[ch]==stack[-1]:
                stack.pop()
            else: 
                return False
        return True if not stack else False
        
        # stack = []
        # if len(s) == 1:
        #     return False
        # for c in s:
        #     if c == "[":
        #         stack.append(']')
        #     elif c == "{":
        #         stack.append('}')
        #     elif c == "(":
        #         stack.append(')')
        #     elif not stack or stack.pop() != c:
        #         return False
        # return not stack
               