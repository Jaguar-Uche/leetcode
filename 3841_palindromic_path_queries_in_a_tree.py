class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
         # 1. Build the tree
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        LOG = n.bit_length()

        parent = [-1] * n
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        prefix = [0] * n

        # 2. Iterative DFS: Euler tour and root-path masks
        timer = 0
        stack = [(0, -1, False)]

        while stack:
            u, p, exiting = stack.pop()

            if exiting:
                tout[u] = timer - 1
                continue

            tin[u] = timer
            timer += 1

            parent[u] = p
            prefix[u] = (prefix[p] if p != -1 else 0) ^ (
                1 << (ord(s[u]) - ord('a'))
            )

            stack.append((u, p, True))

            for v in reversed(graph[u]):
                if v != p:
                    depth[v] = depth[u] + 1
                    stack.append((v, u, False))

        # 3. Binary lifting table
        up = [[0] * n for _ in range(LOG)]
        up[0] = [max(0, p) for p in parent]

        for j in range(1, LOG):
            for u in range(n):
                up[j][u] = up[j - 1][up[j - 1][u]]

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            bit = 0

            while diff:
                if diff & 1:
                    u = up[bit][u]
                diff >>= 1
                bit += 1

            if u == v:
                return u

            for j in range(LOG - 1, -1, -1):
                if up[j][u] != up[j][v]:
                    u = up[j][u]
                    v = up[j][v]

            return up[0][u]

        # 4. Fenwick tree for range XOR updates
        # Subtree intervals use zero-based Euler indices.
        bit = [0] * (n + 2)

        def add(idx, mask):
            idx += 1
            while idx < len(bit):
                bit[idx] ^= mask
                idx += idx & -idx

        def point_query(idx):
            idx += 1
            result = 0

            while idx > 0:
                result ^= bit[idx]
                idx -= idx & -idx

            return result

        def update_subtree(u, mask):
            add(tin[u], mask)
            add(tout[u] + 1, mask)

        # Current character at each node
        chars = list(s)
        ans = []

        # 5. Process queries
        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]

                old_mask = 1 << (ord(chars[u]) - ord('a'))
                new_mask = 1 << (ord(c) - ord('a'))

                if old_mask != new_mask:
                    update_subtree(u, old_mask ^ new_mask)
                    chars[u] = c

            else:
                u = int(parts[1])
                v = int(parts[2])

                w = lca(u, v)

                # Updated root-to-node prefix masks
                pu = prefix[u] ^ point_query(tin[u])
                pv = prefix[v] ^ point_query(tin[v])

                # Restore the LCA's character, which cancels twice
                w_mask = 1 << (ord(chars[w]) - ord('a'))
                path_mask = pu ^ pv ^ w_mask

                # At most one odd-frequency character
                ans.append(
                    path_mask == 0
                    or (path_mask & (path_mask - 1)) == 0
                )

        return ans