"""
1. Two Sum

Given an array of integers, return indices 
of the two numbers such that they add up 
to a specific target.

You may assume that each input would have 
exactly one solution, and you may not use 
the same element twice.
"""

class Solution:
    # Runtime: 48 ms, faster than 95.83% of Python3 online submissions for Two Sum.
    # Memory Usage: 14.1 MB, less than 63.49% of Python3 online submissions for Two Sum.
    def twoSum(self, nums, target):
        # nums : List[int]
        # target: int
        # return: List[int]

        # Create a map
        num_map = {}

        # Iterate over list
        for i in range(len(nums)):
            # The target value minus current list value is our map target
            map_target = target - nums[i]

            # If a record exists for the matching map target, then return the
            # current location and the map target location 
            if num_map.get(map_target) is not None:
                return [num_map.get(map_target), i]
            # Else create a dict entry of our current list value and the current spot
            else:
                num_map[nums[i]] = i
            
if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum([2,7,11,15],9))
    print(solution.twoSum([1,2,3,4,5,6,7],13))
    print(solution.twoSum([2,4,6,7],10))
