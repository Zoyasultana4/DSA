class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(start: int, end: int) -> None:
            while start < end:
                # Swap elements at start and end positions
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        n = len(nums)
        # Handle cases where k > n by taking modulo
        k = k % n
      
        # Step 1: Reverse the entire array
        reverse(0, n - 1)
      
        # Step 2: Reverse the first k elements
        reverse(0, k - 1)
      
        # Step 3: Reverse the remaining n-k elements
        reverse(k, n - 1)
        