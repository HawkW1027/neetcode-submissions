class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)-1):
            prefix *= nums[i]
            res[i+1] = prefix
        subfix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *=subfix
            subfix *= nums[i]
        return res