def maxArea_pruned(height):
    n = len(height)
    if n < 2:
        return 0

    # find two tallest indices without sorting (O(n))
    max1_i = max(range(n), key=lambda i: height[i])
    # temporarily set max2 to some other index
    max2_i = 0 if max1_i != 0 else 1
    for i in range(n):
        if i == max1_i:
            continue
        if height[i] > height[max2_i]:
            max2_i = i

    baseline = min(height[max1_i], height[max2_i]) * abs(max1_i - max2_i)
    best = baseline

    for i, h in enumerate(height):
        if h == 0:
            start = i + 1
        else:
            # only consider j such that h * (j - i) > best
            # so (j - i) > best // h  -> start at i + best // h + 1
            start = i + (best // h) + 1

        j = start
        while j < n:
            area = min(h, height[j]) * (j - i)
            if area > best:
                best = area  # update baseline / best to prune more aggressively
            j += 1

    return best

print(maxArea_pruned([1,1]))