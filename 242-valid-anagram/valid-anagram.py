class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
         # sorted_s = sorted(s)
        # sorted_t = sorted(t)
        # return sorted_s == sorted_t

        #using Hash Map 
        # countS ,  countT = {} , {}
        # if len(s) != len(t):
        #     return False
            
        # for i in range(len(s)):
        #     countS[s[i]] = 1 + countS.get(s[i], 0)
        #     countT[t[i]] = 1 + countT.get(t[i], 0)

        # if countS != countT:
        #     return False
        # return True 
        if len(s) != len(t):
            return False
        count = [0] * 26
        for char in s:
            count[ord(char) - ord('a')] += 1
        print(count)

        for char in t:
            if count[ord(char) - ord('a')] == 0:
                return False
            count[ord(char) - ord('a')] -= 1
        return True
