class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return '0'

        length = 2**n - 1  # Same as 2^n - 1

        if k <= length // 2:
            return self.findKthBit(n - 1, k)
        elif k == (length // 2) + 1:
            return '1'
        else:
            ch = self.findKthBit(n - 1, length - k + 1)  # Handle reversed bit
            return '0' if ch == '1' else '1'  # Handle flipped bit

        