"""
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49

1,8 -> 1

1,8,6 ->  8,6 -> 6

lIdx=0
RIdx=n-1
area = 0

while lIdx < rIdx:
    c_area = min(l,r)* (rIdx - lIdx)
    area = max(area, c_area)
    l < r ? lIdx ++ : rIdx++


"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        lIdx = 0
        rIdx = len(height) - 1

        while lIdx < rIdx:
            currArea = min(height[lIdx],height[rIdx]) * (rIdx - lIdx)
            area = max(area, currArea)
            if height[lIdx] < height[rIdx]:
                lIdx += 1
            else:
                rIdx -= 1
        return area
