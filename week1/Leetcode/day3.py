# LeetCode #3: Move Zeroes
def moveZeroes(nums):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
    nums[slow:] = [0] * (len(nums) - slow)
    return nums

print(moveZeroes([0,1,0,3,12]))

# LeetCode #4: Remove Duplicates
#test1
def removeDuplicates(nums):
    if not nums:
        return 0
    write = 1
    for read in range(1, len(nums)):
        if nums[read] != nums[write - 1]:
            nums[write] = nums[read]
            write += 1
    return write

print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))