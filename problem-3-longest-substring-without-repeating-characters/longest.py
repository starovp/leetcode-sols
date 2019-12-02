"""
3. Longest Substring Without Repeating Characters

Given a string, find the length of the longest
substring without repeating characters.
"""

class Solution(object):
    # Runtime: 32 ms, faster than 96.37% of Python online submissions for Longest Substring Without Repeating Characters.
    # Memory Usage: 12 MB, less than 70.31% of Python online submissions for Longest Substring Without Repeating Characters.
    def lengthOfLongestSubstring(self, s):
        # s: str
        # return: int

        unique = ""
        store = ""
        for x in s:
            if x in unique:
                if len(unique) > len(store):
                    store = unique
                unique = unique[unique.index(x)+1:]
            unique += x
        return max(len(store), len(unique))

if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLongestSubstring("abcabcbb"))
    print(solution.lengthOfLongestSubstring("bbbbb"))
    print(solution.lengthOfLongestSubstring("pwwkew"))
    print(solution.lengthOfLongestSubstring(""))
    print(solution.lengthOfLongestSubstring(" "))
    print(solution.lengthOfLongestSubstring("dvdf"))
