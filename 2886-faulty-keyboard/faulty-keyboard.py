class Solution:
    def finalString(self, s: str) -> str:
        result = []
        s = list(s)
        for char in s:
            if char == 'i':
                l , r = 0, len(result)-1
                while l < r:
                    result[l], result[r] = result[r], result[l]
                    l += 1
                    r -= 1
            else:
                result.append(char)

        return ''.join(result)