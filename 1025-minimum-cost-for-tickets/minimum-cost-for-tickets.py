class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # Dictionary to store the computed minimum costs for each index.
        dp = {}

        # Depth-First Search (DFS) with memoization to calculate the minimum cost.
        def dfs(i):
            # Base case: If we reach the end of the days list, no cost is required.
            if i == len(days):
                return 0

            # If the result for this index is already computed, return it.
            if i in dp:
                return dp[i]

            # Initialize the cost for this index to a very large value (infinity).
            dp[i] = float("inf")

            # Iterate through the options for ticket durations (1-day, 7-day, 30-day).
            for d, c in zip([1, 7, 30], costs):
                # Start a pointer `j` at the current day index `i`.
                j = i
                # Move the pointer forward to skip all days covered by the current ticket.
                while j < len(days) and days[j] < days[i] + d:
                    j += 1
                # Update the minimum cost by considering the current ticket's cost
                # plus the cost of the remaining days (calculated via recursion).
                dp[i] = min(dp[i], c + dfs(j))

            # Return the computed minimum cost for the current index.
            return dp[i]

        # Start the recursion from the first day in the list.
        return dfs(0)
        