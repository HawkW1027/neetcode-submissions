class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x = defaultdict(list)
        y = defaultdict(int)
        for n in nums:
            y[n] += 1
        for key, value in y.items():
            x[value].append(key)
        result = []
        keys = sorted(x.keys(),reverse=True)
        i = 0
        while i<k:
            result.extend(x[keys[i]])
            i += len(x[keys[i]])
        return result

