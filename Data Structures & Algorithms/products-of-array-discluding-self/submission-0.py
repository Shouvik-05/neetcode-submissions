class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if j != i:
                    res[j] *= nums[i]
        return res 
      