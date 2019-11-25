"""
7. Reverse Integer

Given a 32-bit signed integer, reverse digits of an integer.
"""

class Solution:
    # This function does not use string trickiness.
    # Runtime: 24 ms, faster than 98.72% of Python3 online submissions for Reverse Integer.
    # Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Reverse Integer.
    def reverse(self, x):
        # x: int
        # return: int
        neg_check = False

        # Create negative flag
        if x < 0:
            x = abs(x)
            neg_check = True

        # Constantly divide by 10 and append the modulo until we can't
        mod_x = x
        r_list = []
        t_sum = 0
        while mod_x >= 10:
            r_list.append(mod_x%10)
            mod_x=int(mod_x/10)
        r_list.append(mod_x)

        # Add the numbers back, multiplying by powers of 10 appropriately
        ll = len(r_list)
        for i in range(ll):
            t_sum += r_list[i]*(10**(ll-i-1))

        # Multiply by -1 if necessary
        if neg_check:
            t_sum*= -1
            if t_sum < -2147483647:
                return 0

        # Check for overflow
        if t_sum > 2147483647:
            return 0

        return(t_sum)

    # This function converts the result to a string, 
    # reverses using slices, then returns the result.
    # May be slightly simpler to understand but relies on string tricks
    # Runtime: 24 ms, faster than 98.72% of Python3 online submissions for Reverse Integer.
    # Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Reverse Integer.
    def reverse_str(self, x):
        if x < 0:
            num = -1 * int(str(x*-1)[::-1])
        else:
            num = int(str(x)[::-1])
        if num < -2147483647 or num > 2147483647:
            return 0
        else:
            return num

if __name__ == '__main__':
    solution = Solution()

    print(solution.reverse(321))
    print(solution.reverse(-123))
    print(solution.reverse(120))
    print(solution.reverse(10))
    print(solution.reverse(1534236469))

    print(solution.reverse_str(321))
    print(solution.reverse_str(-123))
    print(solution.reverse_str(120))
    print(solution.reverse_str(10))
    print(solution.reverse_str(1534236469))