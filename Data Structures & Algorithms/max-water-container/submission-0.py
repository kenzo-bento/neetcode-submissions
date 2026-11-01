class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum = 0
        lp = 0
        rp = len(heights) - 1
        while lp < rp:
            maximum = max(maximum, min(heights[rp], heights[lp]) * (rp - lp))
            if heights[lp] > heights[rp]:
                rp -= 1
            else:
                lp += 1
        
        return maximum