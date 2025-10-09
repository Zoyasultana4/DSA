class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        longest_palindrome = ""

        def expand_around_center(left, right):
            nonlocal longest_palindrome
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > len(longest_palindrome):
                    longest_palindrome = s[left : right + 1]
                left -= 1
                right += 1

        for i in range(len(s)):
        # Case 1: Odd length palindrome (center is a single character)
            expand_around_center(i, i)
        # Case 2: Even length palindrome (center is between two characters)
            expand_around_center(i, i + 1)

        return longest_palindrome