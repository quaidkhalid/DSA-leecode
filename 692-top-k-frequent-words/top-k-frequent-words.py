class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:# Step 1: Count word frequencies
        count = Counter(words)

        # Step 2: Use a heap with (-frequency, word) to get max-heap behavior
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap)

        # Step 3: Extract top k elements
        result = [heapq.heappop(heap)[1] for _ in range(k)]
        return result
        