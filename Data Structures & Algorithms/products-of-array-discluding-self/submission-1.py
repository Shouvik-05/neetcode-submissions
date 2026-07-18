class Solution:

    def calculate_product(self, n, nums):
        l_pro = r_pro = 1
        # if(n == 0):
        #     l_pro = 1
        # elif(n == (len(nums) - 1)):
        #     r_pro = 1
        # else:
        for j in range (0, n):
            l_pro *= nums[j]
        for k in range (n + 1, len(nums)):
            r_pro *= nums[k]
        return l_pro * r_pro

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(0, len(nums)):
            # for j in range(0, len(nums)):
            #     if j != i:
            #         res[j] *= nums[i]
            res.append(self.calculate_product(i, nums))
        return res 
      