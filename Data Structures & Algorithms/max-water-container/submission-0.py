class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxw=0
        wat=0

        for i in range(len(heights)):
            for j in range(len(heights) - 1, i, -1):
                wat=min(heights[i],heights[j])*(j-i)
                if (wat >maxw):
                    maxw=wat
        return maxw
