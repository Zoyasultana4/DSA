class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)
        for center in range(2 * n - 1):
            left = center // 2
            right = (center + 1) // 2
          
            # Expand around center while characters match
            while left >= 0 and right < n and s[left] == s[right]:
                # Found a palindrome
                count += 1
                # Expand outward
                left -= 1
                right += 1
              
        return count