class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if 0 in nums:
            ans = [0]*len(nums)
            if nums.count(0) == 1:
                zero_idx = nums.index(0)
                nums.remove(0)
                ans[zero_idx] = math.prod(nums)
            return ans

        product = math.prod(nums)
        return [product // i for i in nums]
        