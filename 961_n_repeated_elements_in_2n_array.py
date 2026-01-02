def repeatedNTimes(nums):
    n = len(nums) / 2
    hashmap = {}
    for num in nums:
        if num in hashmap:
            hashmap[num] += 1
        else:
            hashmap[num] = 1
        if hashmap[num] == n:
            return num