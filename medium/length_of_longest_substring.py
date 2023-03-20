"""
Given a string s, find the length of the longest
substring
without repeating characters.

live time to complete (hh:mm:ss): 00 : 18 : 10


Constraints:

    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.

"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_sub = 0
        left_index = 0
        current_substring = ""
        for i in range(len(s)):
            right_letter = s[i]
            if right_letter not in current_substring:
                current_substring += right_letter
                if len(current_substring) > max_sub:
                    max_sub = len(current_substring)
            else:
                # move left side of window to after first instance of dupe
                left_index = left_index + \
                    current_substring.index(right_letter) + 1
                current_substring = s[left_index:i+1]

        return max_sub


if __name__ == "__main__":
    s = Solution()
    strs = ["abcabcbb", "bbbbb", "pwwkew", "aab"]
    for st in strs:
        print(s.lengthOfLongestSubstring(st))
