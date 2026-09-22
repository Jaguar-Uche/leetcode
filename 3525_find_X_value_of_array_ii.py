from typing import List
class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)

        # tree[node] = [product_of_segment, prefix_counts]
        tree = [[1, [0] * k] for _ in range(4 * n)]

        def merge(left, right):
            left_prod, left_count = left
            right_prod, right_count = right

            prod = (left_prod * right_prod) % k
            count = left_count[:]

            for r in range(k):
                new_r = (left_prod * r) % k
                count[new_r] += right_count[r]

            return (prod, count)

        def build(node, l, r):
            if l == r:
                value = nums[l] % k

                tree[node][0] = value
                tree[node][1][value] = 1
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            left = (tree[node * 2][0], tree[node * 2][1])
            right = (tree[node * 2 + 1][0], tree[node * 2 + 1][1])

            prod, count = merge(left, right)

            tree[node][0] = prod
            tree[node][1] = count

        def update(node, l, r, index, value):
            if l == r:
                value %= k

                tree[node][0] = value
                tree[node][1] = [0] * k
                tree[node][1][value] = 1
                return

            mid = (l + r) // 2

            if index <= mid:
                update(node * 2, l, mid, index, value)
            else:
                update(node * 2 + 1, mid + 1, r, index, value)

            left = (tree[node * 2][0], tree[node * 2][1])
            right = (tree[node * 2 + 1][0], tree[node * 2 + 1][1])

            prod, count = merge(left, right)

            tree[node][0] = prod
            tree[node][1] = count

        def query(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                return (tree[node][0], tree[node][1])

            mid = (l + r) // 2

            if qr <= mid:
                return query(node * 2, l, mid, ql, qr)

            if ql > mid:
                return query(node * 2 + 1, mid + 1, r, ql, qr)

            left = query(node * 2, l, mid, ql, qr)
            right = query(node * 2 + 1, mid + 1, r, ql, qr)

            return merge(left, right)

        build(1, 0, n - 1)

        answer = []

        for index, value, start, x in queries:

            # Permanent update
            update(1, 0, n - 1, index, value)

            # Query nums[start ... n-1]
            _, count = query(1, 0, n - 1, start, n - 1)

            answer.append(count[x])

        return answer