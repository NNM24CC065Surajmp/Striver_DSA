class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0

        k = 1   # Number of unique elements found so far

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1

        return k


# Input
nums = list(map(int, input("Enter the numbers: ").split()))

# Create object
sol = Solution()

# Call the method
k = sol.removeDuplicates(nums)

# Output
print("Number of unique elements:", k)
print("Unique elements:", nums[:k])