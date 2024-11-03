class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        concate = s + s # abcdeabcde   cdeab
        if len(s) != len(goal):
            return False
        if goal in concate:
            return True
        else: 
            return False
        