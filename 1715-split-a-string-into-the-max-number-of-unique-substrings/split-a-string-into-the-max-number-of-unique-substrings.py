class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def solve(i, st, curr_count, max_count):
            
            # Pruning for slight improvement
            if curr_count + (len(s) - i) <= max_count[0]:
                return
            
            # Base case: reached end of string
            if i == len(s):
                max_count[0] = max(max_count[0], curr_count)
                return
            
            # Iterate over substrings
            for j in range(i, len(s)):
                sub = s[i:j+1]
                if sub not in st:
                    st.add(sub)
                    solve(j+1, st, curr_count+1, max_count)
                    st.remove(sub)

        # Initialize variables
        max_count = [0]
        st = set()
        solve(0, st, 0, max_count)
        
        return max_count[0]