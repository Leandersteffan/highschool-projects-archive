def searchRange(nums, target):
    starting_pos = -1
    ending_pos = -1
    m = len(nums)
    if m!=0 and nums[0] <= target and nums[m - 1] >= target:
        for i in range(m):
            if starting_pos == -1:
                if nums[i] == target:
                    starting_pos, ending_pos = i, i
            elif nums[i] == target:
                ending_pos = i
            else:
                break
    return [starting_pos, ending_pos]


    '''if not nums or not target in nums:
        return [-1, -1]
    x = int(len(nums) / 2)
    while nums[x] != target:
        """if len(nums) < 2:
            return [-1, -1]"""
        if nums[x] > target:
            """if int(len(nums[:x]) / 2) == 0:
                return [-1, -1]"""
            x -= int(len(nums[:x]) / 2)
            if int(len(nums[:x]) / 2) == 0:
                x -= 1
        elif nums[x] < target:
            """if int(len(nums[x:]) / 2) == 0:
                return [-1, -1]"""
            x += int(len(nums[x:]) / 2)
            if int(len(nums[x:]) / 2) == 0:
                x += 1
    l, r = x, x
    while nums[l - 1] == target and l - 1 >= 0:
        l -= 1
    try:
        while nums[r + 1] == target:
                r += 1
    except IndexError:
        pass
    return [l, r]'''



print(searchRange([1, 3], 1))
print(searchRange([1, 2, 3, 4, 5, 6, 6, 7], 6))
