class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_s = sorted(set(nums))
        count = 1
        res = 1
        for i in range(len(nums_s)-1):
            if nums_s[i+1] == nums_s[i]+1:
                count += 1
                if count > res:
                    res = count
            else:
                count = 1
        return res