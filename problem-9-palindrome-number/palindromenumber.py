"""
9. Palindrome Number

Determine whether an integer is a palindrome. 
An integer is a palindrome when it reads the same backward as forward.
"""

class Solution:
    # Runtime: 44 ms, faster than 99.47% of Python3 online submissions for Palindrome Number.
    # Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Palindrome Number.
    def isPalindrome(self, x):
        # x: int
        # return: bool

        # All negative numbers and multiples of 10 are not palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        """
        To validate a palindrome we can compare the 
        second half of the number to the first half.
        We do this by building the second half through
        mod and multiplying the existing half by 10.
        
        At the same time, divide our original number
        by 10. When the original is smaller than the
        second half, we have officially separated our 
        number into two. 

        Finally, compare the two. If there is a middle
        integer, we can ignore it as any middle integer
        does not contribute to the "palindromeness" of a 
        number. 121 does not care about the 2, just as
        in 12421 we do not care about the 4.

        e.g. 121 -> 
        t_num = 1 + 10* 0 = 1, x//10 = 12; 
        t_num = 2 + 10*1 = 12, x//10 = 1
        eval 12 != 1 or 1 == 1 -> True
        """
        t_num = 0
        while (x > t_num):
            t_num = 10*t_num + x%10
            x = x//10

        return(x == t_num or x == t_num//10)


if __name__ == '__main__':
    solution = Solution()
    print(solution.isPalindrome(121))
    print(solution.isPalindrome(-121))
    print(solution.isPalindrome(10))
    print(solution.isPalindrome(11))