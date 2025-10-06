from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Early return if strings have different lengths
        if len(s) != len(t):
            return False
      
        # Count frequency of each character in string s
        char_count = Counter(s)
      
        # Iterate through string t and decrement character counts
        for char in t:
            char_count[char] -= 1
            # If count goes negative, t has more of this character than s
            if char_count[char] < 0:
                return False
      
        # All characters matched successfully
        return True