
target = 9
nums = list(map(int, input("Enter the numbers:").split()))
           
def two_sum(nums,target):
    for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
result = two_sum(nums,target)
print(result)