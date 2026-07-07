class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        for i in range(len(nums)):
            for j, num in enumerate(nums):
                if j != i:
                    res[i] *= num

        return res