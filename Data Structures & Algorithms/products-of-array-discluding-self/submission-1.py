class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res, prod, zero_count, j = [], 1, 0, 0

        def countZero():
            nonlocal zero_count
            for num in nums:
                if num == 0:
                    zero_count += 1

        countZero()
        if zero_count > 1:
            return [0] * len(nums)
       
        for i, num in enumerate(nums):
            if num != 0:
                prod *= num
            else:
                j = i
        
        if zero_count == 1:
            res = [0] * len(nums)
            res[j] = prod
            return res

        for num in nums:
            res.append(int(prod / num) if num != 0 else prod)
    
        return res