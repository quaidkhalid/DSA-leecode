class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        # stack = []
        # i = 0
        # for item in pushed:
        #     stack.append(item)
        #     while stack and stack[-1] == popped[i]:
        #         stack.pop()
        #         i += 1
        # if not stack:
        #     return True
        # else:
        #     return False
        stack = []
        index = 0

        for val in pushed:
            stack.append(val)

            while stack and stack[-1] == popped[index]:
                 stack.pop()
                 index += 1

        return len(stack) == 0
        