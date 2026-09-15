class Solution:
    def maxArea(self, heights: list[int]) -> int:
        i, j = 0, len(heights) - 1
        res = 0

        while i < j:
            h_left, h_right = heights[i], heights[j]
            res = max(res, min(h_left, h_right) * (j - i))

            if h_left <= h_right:
                # Advance i until finding a strictly taller bar
                while i < j and heights[i] <= h_left:
                    i += 1
            else:
                # Advance j until finding a strictly taller bar
                while i < j and heights[j] <= h_right:
                    j -= 1

        return res