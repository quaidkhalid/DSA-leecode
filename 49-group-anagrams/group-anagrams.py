class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictt = {}
        for s in strs:
            f = str(sorted(s))
            if f not in dictt:
                dictt[f] = []
            dictt[f].append(s)
        return list(dictt.values())
        