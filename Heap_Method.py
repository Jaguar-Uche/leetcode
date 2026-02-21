class MinHeap:
    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)
        self._bubble_up(len(self.data) - 1)

    def pop(self):
        if not self.data:
            return None

        self._swap(0, len(self.data) - 1)
        item = self.data.pop()
        self._bubble_down(0)
        return item

    def _bubble_up(self, i):
        while i > 0:
            p = (i - 1) // 2
            if self.data[i] < self.data[p]:
                self._swap(i, p)
                i = p
            else:
                break

    def _bubble_down(self, i):
        n = len(self.data)
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i

            if left < n and self.data[left] < self.data[smallest]:
                smallest = left
            if right < n and self.data[right] < self.data[smallest]:
                smallest = right

            if smallest == i:
                break

            self._swap(i, smallest)
            i = smallest

    def _swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def __bool__(self):
        return bool(self.data)