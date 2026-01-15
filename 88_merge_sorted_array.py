def merge(nums1, m: int, nums2, n: int) -> None:
    nums1.extend(nums2)
    nums1.sort()
    del nums1[:n]

merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)

