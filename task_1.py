def searchRange(nums, target):
    def binarySearchLeft(nums, target):
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

    def binarySearchRight(nums, target):
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return left - 1

    left_index = binarySearchLeft(nums, target)

    if left_index == len(nums) or nums[left_index] != target:
        return [-1, -1]

    right_index = binarySearchRight(nums, target)

    return [left_index, right_index]


print(searchRange([5, 7, 7, 8, 8, 10], 8))  # Output: [3, 4]
print(searchRange([5, 7, 7, 8, 8, 10], 6))  # Output: [-1, -1]
print(searchRange([], 0))  # Output: [-1, -1]
