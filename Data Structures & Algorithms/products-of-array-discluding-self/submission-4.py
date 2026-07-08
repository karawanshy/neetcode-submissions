class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref, res = [1] * n, [1] * n

        for i in range(1, n):
            pref[i] = pref[i-1] * nums[i-1]
        
        for i in range(n - 2, -1, -1):
            res[i] = res[i+1] * nums[i+1]
        
        for i in range(n):
            res[i] = pref[i] * res[i]
        
        return res