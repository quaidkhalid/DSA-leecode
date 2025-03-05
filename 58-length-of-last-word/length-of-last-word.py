class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # word = ''
        # words = []
        # for i in range(len(s)):
        #     if s[i] != ' ':
        #         word += s[i]
        #     elif word:
        #         words.append(word)
        #         word = ''
        # if word:
        #     words.append(word)

        # return len(words[-1]) if words else 0

        # words = s.split()
        # return len(words[-1])
        count = 0
        i = len(s)-1
        while i >=0 and s[i] == " ":
            i -= 1
        while i>=0 and s[i] != " ":
            count +=1
            i -=1
        return count
        