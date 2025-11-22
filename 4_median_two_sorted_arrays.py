def findMedianSortedArrays(nums1, nums2):
    new_list  = [ x for this_list in [nums1, nums2] for x in this_list]
    # new_set = set(new_list)
    # new_list  = list(new_set)
    # new_list.sort()

    if len(new_list) % 2 == 0:
        middle = len(new_list) // 2
        median = (new_list[middle] + new_list[middle - 1])/2
    else:
        middle = len(new_list)-1 // 2
        median = new_list[middle]

    return median

print(findMedianSortedArrays([1,2,3], [4,5,6,7,8]))