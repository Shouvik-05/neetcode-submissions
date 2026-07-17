class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}

        for n in nums:
            key = n
            if key not in res:
                res[key] = 1
            else:
                res[key] += 1

        ressort = sorted(res.items(), key=lambda x: x[1], reverse=True)

        first_k = ressort[0:k]

        ans = []
        for item in first_k:
            ans.append(item[0])
        return ans
