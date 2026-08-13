class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = [0]*len(nums)
        product = 1
        count = 0

        for num in nums:
            if num == 0:
                count += 1
        if count >= 2:
            return arr 
            
        for num in nums:
            if  num != 0:
                product *= num
            else:
                continue
        
        for i in range(len(nums)):
            if nums[i] == 0:
                arr[i] = product
                return arr
            else:
                nums[i] = product // nums[i]

        return nums

        