class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i,j = 0,len(heights)-1
        res = 0
        while i < j:
            h_l = heights[i]
            h_r = heights[j]
            res = max(res, min(h_l, h_r) * (j - i))
            if h_l < h_r:
                while i < j & heights[i] <= h_l:
                    i += 1
            else:
                while j > i & heights[j] <= h_r:
                    j -= 1
        return res