class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        result = [0] * n
        
        # Traverse temperatures from right to left
        for i in range(n - 1, -1, -1):
            # Remove indices from stack while current temperature is greater or equal
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()
            
            # If stack is not empty, calculate the difference in days
            if stack:
                result[i] = stack[-1] - i
            
            # Push current index to stack
            stack.append(i)
        
        return result

        