class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = defaultdict(set)

        for num in nums:
            if num in res:
                res[num] += 1
            else:
                res[num] = 1
            
        for key in res:
            if res[key] > len(nums)/2:
                return key