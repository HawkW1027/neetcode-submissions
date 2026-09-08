class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num_of_zero,total_except_zero = 0,1
        res = [0] * len(nums)
        for num in nums:
            if num:
                total_except_zero *= num
            else:
                num_of_zero += 1
        if num_of_zero > 1:
            return res
        if num_of_zero == 1:
            for i,num in enumerate(nums):
                if not num:
                    res[i] = total_except_zero
                    return res
        if num_of_zero == 0:
            for i ,num in enumerate(nums):
                res[i] = int(total_except_zero/num)
            return res
