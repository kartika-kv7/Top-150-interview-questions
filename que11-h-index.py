class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        count = [0] * (n + 1)
        for c in citations:
            if c >= n:
                count[n] += 1
            else:
                count[c] += 1
        cumulative = 0
        for h in range(n, -1, -1):
            cumulative += count[h]
            if cumulative >= h:
                return h
            