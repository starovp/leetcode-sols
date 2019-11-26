"""
26. Remove Duplicates from Sorted Array

Given a sorted array nums, remove the duplicates in-place such that 
each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying 
the input array in-place with O(1) extra memory.
"""

class Solution:
    # Runtime: 84 ms, faster than 95.52% of Python3 online submissions for Remove Duplicates from Sorted Array.
    # Memory Usage: 14.4 MB, less than 100.00% of Python3 online submissions for Remove Duplicates from Sorted Array.
    def removeDuplicates(self, nums):
        # nums: List[int]
        # return: int

        length = len(nums)

        # Arrays of none or one values do not need to be de-duplicated
        if length in (0,1):
            return length
        
        # Keep track of uniques
        unique = 0

        # Iterate over list.
        # If the next value is different from current, this marks the end 
        # of repetitions of the current value, and we can set it to the 
        # unique counter's position. 
        # In this way, all values behind current will be uniques in order. 
        for i in range(length-1):
            if nums[i] != nums[i+1]:
                nums[unique] = nums[i]
                unique += 1 
        
        # Thus the i+1 value from above is unique too, 
        # and is placed at the next position. 
        nums[unique] = nums[length-1]

        # Slice list to include only uniques
        nums = nums[:unique+1]

        return len(nums)

if __name__ == '__main__':
    solution = Solution()
    print(solution.removeDuplicates([1,1,2]))
    print(solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
    print(solution.removeDuplicates([1,1]))
    print(solution.removeDuplicates([1,1,1]))