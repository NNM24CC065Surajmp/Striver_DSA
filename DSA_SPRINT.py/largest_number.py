class Solution:
    def largestElement(self, nums):
        largest = nums[0]

        for i in range(len(nums)):
            if nums[i] > largest:
                largest = nums[i]

        return largest


print("Enter the list of numbers separated by space:")
nums = list(map(int, input().split()))

sol = Solution()
print(sol.largestElement(nums))