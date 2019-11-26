"""
20. Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.
"""

class Solution:
    # Runtime: 32 ms, faster than 82.66% of Python3 online submissions for Valid Parentheses.
    # Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Valid Parentheses.
    def isValid(self, s):
        # s: str
        # return: bool

        # Create map of matching parentheses
        match_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []

        # Traverse string
        for i in range(len(s)):
            # Top of stack is assigned or non-element value if stack empty
            top = stack[-1] if stack else 'X'

            # If opening bracket, append to the top of stack
            if s[i] in match_map.values():
                stack.append(s[i])

            # If current parenthesis doesn't match the top of stack, break
            elif top != match_map[s[i]]:
                return False

            # Otherwise it's valid and we eliminate that parenthesis from stack
            else:
                stack.pop()

        return len(stack)==0

if __name__ == '__main__':
    solution = Solution()
    print(solution.isValid("()"))
    print(solution.isValid("()[]{}"))
    print(solution.isValid("(]"))
    print(solution.isValid("([)]"))
    print(solution.isValid("["))
    print(solution.isValid("]"))
