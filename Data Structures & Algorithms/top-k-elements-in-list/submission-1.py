class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x = defaultdict(list)
        y = defaultdict(int)
        for n in nums:
            y[n] += 1
        for key, value in y.items():
            x[value].append(key)
        result = []
        keys = heapq.nlargest(k,x)
        for key in keys:
            result.extend(x[key])
        return result

