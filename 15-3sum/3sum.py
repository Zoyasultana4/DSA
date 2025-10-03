class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()  # Sort the array to enable the two-pointer approach and handle duplicates

        for i, a in enumerate(nums):
            # Optimization: If the current number is positive, future numbers will also be positive (due to sorting),
            # so no triplet can sum to zero.
            if a > 0:
                break

            # Skip duplicate values for the first element 'a'
            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1  # Initialize left and right pointers
            while l < r:
                threeSum = a + nums[l] + nums[r]

                if threeSum > 0:
                    r -= 1  # Sum is too large, decrease the right pointer
                elif threeSum < 0:
                    l += 1  # Sum is too small, increase the left pointer
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    # Skip duplicate values for the left pointer
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res
