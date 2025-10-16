class Solution:
    def hammingWeight(self, n: int) -> int:
        binary_representation = bin(n)  # Converts to binary string, e.g., '0b101'
        return binary_representation.count('1')

# Example usage:
#number = 9  # Binary is 1001, so 2 set bits
#print(f"Number of 1 bits in {number} (string method): {count_set_bits_str(number)}")