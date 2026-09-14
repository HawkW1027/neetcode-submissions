class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        res_set = set()
        res = []
        while i < len(nums)-2:
            j = i+1
            while j < len(nums)-1:
                k = j+1
                while k < len(nums):
                    if nums[i]+nums[j]+nums[k] == 0:
                        res_set.add(tuple(sorted([nums[i],nums[j],nums[k]])))
                    k += 1
                j += 1
            i += 1
        res = list(res_set)
        return res