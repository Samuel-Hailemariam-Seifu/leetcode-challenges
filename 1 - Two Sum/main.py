"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
"""

# Brute Force Solution - O(n²) time complexity
class Solution(object):
    def twoSum(self, nums, target):
        new_list = []

        for x in range(0, len(nums)):
            for y in range(0,len(nums)):
                if(x == y):
                    continue
                if nums[x] + nums[y] == target:
                    print(nums[x] + nums[y])
                    new_list.append(x)
                    new_list.append(y)
                    return new_list

# Optimized Solution using Hash Map - O(n) time complexity
class SolutionOptimized(object):
    def twoSum(self, nums, target):
        # Hash map to store number -> index mapping
        num_map = {}
        
        for i, num in enumerate(nums):
            # Calculate what number we need to find
            complement = target - num
            
            # Check if we've already seen the complement
            if complement in num_map:
                print(f"Found: {num} + {complement} = {target}")
                return [num_map[complement], i]
            
            # Store current number and its index
            num_map[num] = i
        
        return []  # No solution found

# Test cases
nums1 = [2,7,11,15]
target1 = 9
nums2 = [3,2,4]
target2 = 6
nums3 = [3,3]
target3 = 6

print("=== Brute Force Solution ===")
solution = Solution()
print("Test 1:", solution.twoSum(nums1, target1))
print("Test 2:", solution.twoSum(nums2, target2))
print("Test 3:", solution.twoSum(nums3, target3))

print("\n=== Optimized Hash Map Solution ===")
solution_opt = SolutionOptimized()
print("Test 1:", solution_opt.twoSum(nums1, target1))
print("Test 2:", solution_opt.twoSum(nums2, target2))
print("Test 3:", solution_opt.twoSum(nums3, target3))
