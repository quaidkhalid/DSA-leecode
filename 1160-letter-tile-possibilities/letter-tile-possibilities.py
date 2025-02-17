class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        result = set()
        used = [False] * len(tiles)

        # Generate all possible sequences including empty string
        self.solve(tiles, "", used, result)

        # Subtract 1 to exclude empty string from count
        return len(result) - 1

    def solve(self, tiles, current, used, result):
        result.add(current)

        # Try adding each unused character to current sequence
        for pos, char in enumerate(tiles):
            if not used[pos]:
                used[pos] = True
                self.solve(tiles, current + char, used, result)
                used[pos] = False
        