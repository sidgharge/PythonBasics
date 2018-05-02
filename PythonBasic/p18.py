
nums = []
for i in range(3):
    print("Enter number ", i + 1, ": ")
    nums.append(int(input()))

if nums[0] == nums[1] == nums[2]:
    print(nums[0] * 3 * 3)
else:
    print(nums[0] + nums[1] + nums[2])
