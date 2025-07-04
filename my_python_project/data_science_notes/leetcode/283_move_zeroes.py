class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start = 0
        end = 1
        if len(nums) == 1:
            return
        while end != len(nums) and start != len(nums) :
            if nums[start] == 0 and nums[end] != 0:
                nums[start],nums[end] = nums[end], nums[start]
            if nums[start] != 0 and nums[end] != 0:
                start +=1
                end +=1
            elif nums[start] != 0 : 
                start +=1
            elif nums[end] == 0 :
                end +=1
