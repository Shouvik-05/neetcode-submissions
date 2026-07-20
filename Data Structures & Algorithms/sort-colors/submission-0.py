class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count0 = 0
        count1 = 0
        count2 = 0
        for num in nums:
            if num == 0:
                count0 += 1
                continue
            if num == 1:
                count1 += 1
                continue
            if num == 2:
                count2 += 1
                continue
        
        for i in range(0, len(nums)):
            if count0 != 0:
                nums[i] = 0
                count0 -=1
                continue
            if count1 != 0:
                nums[i] = 1
                count1 -=1
                continue
            if count2 != 0:
                nums[i] = 2
                count2 -=1
                continue