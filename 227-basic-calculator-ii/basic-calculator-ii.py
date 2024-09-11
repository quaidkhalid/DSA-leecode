class Solution:
    def calculate(self, s: str) -> int:
            
        curr = 0
        ans = 0
        op = '+'
        s += '+'
        stk = []

        for i in range(len(s)):
            if s[i].isdigit():
                curr = curr * 10 + int(s[i])
            elif s[i] == ' ':
                continue
            else:
                if op == '+':
                    stk.append(curr)
                elif op == '-':
                    stk.append(-curr)
                elif op == '*':
                    num = stk.pop()
                    stk.append(num * curr)
                else:  # for division
                    num = stk.pop()
                    if num < 0:
                        stk.append(-(-num // curr))  # to handle division for negative numbers correctly
                    else:
                        stk.append(num // curr)
                
                curr = 0
                op = s[i]
        
        while stk:
            ans += stk.pop()
        
        return ans
