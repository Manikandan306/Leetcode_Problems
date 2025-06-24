class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_from_center(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]  # slice after overshooting

        longest = ""
        for i in range(len(s)):
            # Odd length palindrome (single center)
            odd = expand_from_center(i, i)
            # Even length palindrome (double center)
            even = expand_from_center(i, i + 1)

            # Pick the longer one
            current_longest = odd if len(odd) > len(even) else even

            # Update result if current is longer
            if len(current_longest) > len(longest):
                longest = current_longest

        return longest
