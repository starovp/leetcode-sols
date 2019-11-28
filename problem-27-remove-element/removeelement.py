"""
27. Remove Element

Given an array nums and a value val, 
remove all instances of that value 
in-place and return the new length.

Do not allocate extra space for another array, 
you must do this by modifying the input 
array in-place with O(1) extra memory.

The order of elements can be changed. 
It doesn't matter what you leave beyond 
the new length.

"""

class Solution:
    # Runtime: 20 ms, faster than 99.92% of Python3 online submissions for Remove Element.
    # Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Remove Element.
    def removeElement(self, nums, val):
        # nums: List[int]
        # val: int
        # return: int

        j = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1

        nums = nums[:j]

        return len(nums)
        
if __name__ == '__main__':
    solution = Solution()
    print(solution.removeElement([3,2,2,3],3))
    print(solution.removeElement([0,1,2,2,3,0,4,2],2))
