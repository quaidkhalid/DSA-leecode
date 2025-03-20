class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" : return ""

        count_t = {}
        window = {}

        for i in range(len(t)):
            count_t[t[i]] = 1 + count_t.get(t[i], 0)

        have, need = 0, len(count_t)
        result, res_len = [-1, -1], float("infinity")

        left = 0

        for right in range(len(s)):
            window[s[right]] = 1 + window.get(s[right], 0)

            if s[right] in count_t and window[s[right]] == count_t[s[right]]:
                have += 1
            
            while have == need:
                if (right - left + 1) < res_len:
                    result = [left, right]
                    res_len = right - left + 1
                
                window[s[left]] -= 1

                if s[left] in count_t and window[s[left]] < count_t[s[left]]:
                    have -= 1
                
                left += 1
        
        left, right = result
        return s[left:right+1] if res_len != float("infinity") else ""
        