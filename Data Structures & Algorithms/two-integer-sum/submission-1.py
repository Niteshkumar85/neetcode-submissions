class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Brute force approach
        # for i in range(len(nums)):
        #     for j in range(i+1 , len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]

        # Optimal approach 

        seen = {}

        for i, num in enumerate(nums):
            rem = target - num

            if rem in seen:
                return [seen[rem],i]
            seen[num] = i                
