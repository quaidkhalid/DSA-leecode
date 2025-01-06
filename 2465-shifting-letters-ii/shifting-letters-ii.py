class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        diff = [0] * n
        for query in shifts:
            L = query[0]
            R = query[1]
            dir = query[2]

            if dir == 0:
                x = -1
            else:
                x = 1

            diff[L] += x
            if R+1 < n:
                diff[R+1] -= x

        # cumulative sum
        for i in range(1,n):
            diff[i] += diff[i - 1]

    
        # applying shift
        s = list(s)

        for i in range(n):
            shift = diff[i] % 26
            if shift < 0:
                shift += 26

            # Perform the character shift
            s[i] = chr(((ord(s[i]) - ord('a') + shift) % 26) + ord('a'))

        # Convert back to string

        return ''.join(s)
        