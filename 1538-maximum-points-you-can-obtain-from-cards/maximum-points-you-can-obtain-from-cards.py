class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        lsum = 0
        for i in range(k):
            lsum +=cardPoints[i]

        maxsum = lsum
        rsum = 0
        j = len(cardPoints)-1
        for k in range(k-1,-1,-1):
            lsum -= cardPoints[k]
            rsum += cardPoints[j]
            j -= 1
            maxsum = max(maxsum, lsum+rsum)

        return maxsum
        