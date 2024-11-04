class Solution:
    def compressedString(self, word: str) -> str:
        n = len(word)
        comp = ""
        i = 0
        while i < n:
            count = 0
            ch = word[i]
            while i < n and count < 9 and word[i] == ch:
                count += 1
                i += 1
            comp = comp + str(count) + ch
        return comp
        