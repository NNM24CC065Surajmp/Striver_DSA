def duplicate_found(nums):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False

nums = list(map(int, input("Enter the numbers:").split()))
if duplicate_found(nums):
    print("Duplicate found")
else:
    print("No duplicates found")
