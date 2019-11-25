"""
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
All given inputs are in lowercase letters a-z.
"""

class Solution:
    # Runtime: 32 ms, faster than 92.33% of Python3 online submissions for Longest Common Prefix.
    # Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Longest Common Prefix.
    def longestCommonPrefix(self, strs):
        # strs: List[str]
        # return: str
        if len(strs) == 0:
            return ""

        # We only need to care as far as the smallest word in the list.
        smallest = min(strs, key=len)

        # Iterate through the smallest word
        for i, g in enumerate(smallest):
            # g is fixed on letter of smallest word,
            # comparing iterating value with g.
            for word in strs:
                # Return smallest up to i if there's a mismatch.
                if word[i] != g:
                    return smallest[:i]
        return smallest

if __name__ == '__main__':
    solution = Solution()
    print(solution.longestCommonPrefix(["flower","flow","flight"]))
    print(solution.longestCommonPrefix(["dog","racecar","car"]))
    print(solution.longestCommonPrefix([]))