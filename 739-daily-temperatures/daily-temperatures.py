class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        result = [0] * n

        for i in range(n-1, -1,-1):
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()

            if not stack:
                result[i] = 0
            else:
                result[i] = stack[-1] - i

            stack.append(i)

        return result

            


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # n = len(temperatures)
        # stack = []
        # result = [0] * n
        
        # # Traverse temperatures from right to left
        # for i in range(n - 1, -1, -1):
        #     # Remove indices from stack while current temperature is greater or equal
        #     while stack and temperatures[i] >= temperatures[stack[-1]]:
        #         stack.pop()
            
        #     if not stack:
        #         result[i] = 0
        #     else:
        #         result[i] = stack[-1] - i
            
        #     # Push current index to stack
        #     stack.append(i)
        
        # return result

        