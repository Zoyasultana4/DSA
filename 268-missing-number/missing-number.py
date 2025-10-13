class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        missing_num = 0
        for i in range(n + 1):
            missing_num ^= i
        
        for num in nums:
            missing_num ^= num
            
        return missing_num   