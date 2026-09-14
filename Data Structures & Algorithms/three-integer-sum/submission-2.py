class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i,n in enumerate(nums):
            j = i + 1
            k = len(nums)-1
            while j < k:
                if n + nums[j] + nums[k]==0 :
                    res.add(tuple([n,nums[j],nums[k]]))
                j += 1
                k -= 1
        return(list(res))