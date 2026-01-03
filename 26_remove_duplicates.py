def removeDuplicates(nums) -> int:
    # nums = set(nums)
    # nums = list(nums)
    #
    x = len(set(nums))
    previous = nums[0]
    i = 1
    while len(nums) > x:
        if nums[i] == previous:
            previous = nums.pop(i)
            # print(f"This is iteration {i} nums is {nums}")
            i-=1
        else:
            previous = nums[i]
        i+=1

    print(nums)

    return x

print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))