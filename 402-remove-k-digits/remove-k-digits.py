class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # stack = []
        # for c in num:
        #     while k>0 and stack and stack[-1] > c:
        #         k -= 1
        #         stack.pop()
        #     stack.append(c)

        # stack = stack[:len(stack)-k]

        # res = ''.join(stack).lstrip('0')

        # return res if res else '0'
        stack = []
        if k>len(num):
            return 0

        for digit in num:
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1

            stack.append(digit)

        while (k > 0):
            stack.pop()
            k -= 1

        result = ''.join(stack).lstrip('0')
    
        return result if result else '0'