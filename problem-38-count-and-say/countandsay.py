"""
38. Count and Say

The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

"""

class Solution(object):
    # Runtime: 16 ms, faster than 92.48% of Python online submissions for Count and Say.
    # Memory Usage: 11.9 MB, less than 48.15% of Python online submissions for Count and Say.
    def countAndSay(self, n):
        # n: int
        # return: str
        
        # Set unique tracker, first string, and init empty string
        unique = 0
        num_str = "11 "
        new_str = ""

        if n == 1:
            return "1"
            
        for j in range(2,n):
            # Go over the input sequence
            for i in range(len(num_str)-1):
                # If next num is different, count the incidence of current number
                # over the sequence of duplicates since the last set of duplicates,
                # defined by num_str[unique:i]
                if num_str[i] != num_str[i+1]:
                    ct = num_str[unique:i+1].count(num_str[i])
                    unique = i
                    new_str += str(ct)+str(num_str[i])
            num_str = new_str+" "
            new_str = ""
            unique = 0
            
        # Remove trailing space from output string
        num_str = num_str[:len(num_str)-1]
        return(num_str)

if __name__ == '__main__':
    solution = Solution()
    print(solution.countAndSay(1))      
    print(solution.countAndSay(2))      
    print(solution.countAndSay(3))     
    print(solution.countAndSay(4))
    print(solution.countAndSay(5))
    print(solution.countAndSay(6))
