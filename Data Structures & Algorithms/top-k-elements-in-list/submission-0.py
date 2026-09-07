class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x = defaultdict(int)
        for n in nums:
            x[n] += 1
        inverted = {v:k for k,v in x.items()}
        result: list[int]=[]
        top_k_keys = heapq.nlargest(k, inverted)
        for m in top_k_keys:
            result.append(inverted[m])
        return result

