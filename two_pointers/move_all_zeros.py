"""
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

[0,1,0,3,12]

zeroCtr = 2
[1,3,12]
-----
[1,3,12,0,0]


---------------

[0,1,0,3,12]
ptr=0
[1,0,0,3,12]
ptr=1

[1,3,0,0,12]
ptr=2


[1,3,12,0,0]
ptr=3

"""


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroPtr = 0
        for i in range(len(nums)):

            if nums[i] != 0:
                nums[zeroPtr], nums[i] = nums[i], nums[zeroPtr]
                zeroPtr += 1
