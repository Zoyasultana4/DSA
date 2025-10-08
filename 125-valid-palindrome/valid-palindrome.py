class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
        # Move left pointer past non-alphanumeric characters
            while left < right and not s[left].isalnum():
                left += 1
        # Move right pointer past non-alphanumeric characters
            while left < right and not s[right].isalnum():
                right -= 1

        # Compare characters, converting to lowercase for case-insensitivity
            if s[left].lower() != s[right].lower():
                return False

        # Move pointers inwards
            left += 1
            right -= 1

        return True