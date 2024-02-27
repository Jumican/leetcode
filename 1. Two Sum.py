nums = [2, 4, 7, 8, 6, 9, 1]
target = 8

i = 0
while i != len(nums) - 1:
    j = i+1
    while j != len(nums):
        if nums[i] + nums[j] == target and i != j:
            x = [i, j]
            print(x)

        j += 1

    i += 1
