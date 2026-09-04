class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        empty_dict = {}
        for i,n in enumerate(nums):
            diff = target-n
            if diff in empty_dict:
                return [empty_dict[diff], i]
            empty_dict[n]=i