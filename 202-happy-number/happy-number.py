class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n != 1 and n not in visited:
            # Add current number to visited set
            visited.add(n)
          
            # Calculate sum of squares of digits
            sum_of_squares = 0
            while n > 0:
                # Extract last digit using divmod
                n, digit = divmod(n, 10)
                # Add square of digit to sum
                sum_of_squares += digit * digit
          
            # Update n with the new sum for next iteration
            n = sum_of_squares
      
        # Return True if we reached 1, False if we found a cycle
        return n == 1