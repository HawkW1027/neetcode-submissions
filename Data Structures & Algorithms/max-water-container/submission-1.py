class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i,j = 0,len(heights)-1
        res = 0
        while i < j:
            area = min(heights[i],heights[j]) * (j-i)
            if area > res:
                res = area
            if heights[i] < heights[j]:
                while (i < j) & (heights[i] > heights[i+1]):
                    i += 1
                    area = min(heights[i],heights[j]) * (j-i)
                    if i == j:
                        return max(res,area)
            if heights[i] > heights[j]:
                while (j > i) & (heights[j] > heights[j-1]):
                    j -= 1
                    if j == i:
                        return max(res,area)
            i += 1
        return res