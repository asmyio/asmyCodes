# Two Sum
"""
Question: 
Given array of integers (num), integer target (target).
return indices of the two numbers that adds up to the target.
Tips: Don't use the same element twice.

"""

"""
Solution: HashMaps
- saves the one's we did before
- matches the required diff that's needed within the saved map
- to achieve the pairs for the two numbers that adds up to the target
"""

# Brute Force: n times for each number is O(n^2) which is the worst
# HashMaps: mapping the value to the index, it won't use the same value twice
# init: hashmap is empty
# as we minus, we add it to the hashmap

# the reason is why HashMap is the best choice because it is not repeatable,
# time: O(n) memory: O(n)

# val: 2, index: 0
# val: 1, index 1
# val: 5, index 2

# one pass solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # value: index
        for i, n in enumerate(nums):
            diff = target - n 
            if diff in prevMap: #check if the difference is inside the hashmap
                return [prevMap[diff], i]
            prevMap[n] = i