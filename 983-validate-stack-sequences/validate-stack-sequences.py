class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0
        for item in pushed:
            stack.append(item)
            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1
        if not stack:
            return True
        else:
            return False
        