class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0  # Initialize the result
        for i in range(32):
            # Extract the i-th bit from n (from right to left)
            bit = (n >> i) & 1
            ans |= (bit << (31 - i))
        return ans 