
class MinHeap():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.count = len(data)

    def _shift_up(self, index):
        if index > 0:
            parent = (index - 1) // 2
            if self.data[index] > self.data[parent]:
                self.data[index], self.data[parent] = self.data[parent], self.data[index]
                self._shift_up(parent)

    def _shift_down(self, index):
        if index < self.count:
            left = 2 * index + 1
            right = 2 * index + 2
            if left < self.count and right < self.count and self.data[left] < self.data[index] and self.data[left] < self.data[right]:
                self.data[index], self.data[left] = self.data[left], self.data[index]  # 交换得到较小的值
                self._shift_down(left)
            elif left < self.count and right < self.count and self.data[right] < self.data[left] and self.data[right] < self.data[index]:
                self.data[right], self.data[index] = self.data[index], self.data[right]
                self._shift_down(right)
            # 特殊情况： 如果只有做叶子结点
            if left < self.count < right and self.data[left] < self.data[index]:
                self.data[left], self.data[index] = self.data[index], self.data[left]
                self._shift_down(left)

    def append(self, v):
        self.data.append(v)
        self._shift_up(self.count)
        self.count += 1

    def pop(self):
        self.count -= 1
        v = self.data.pop()
        self._shift_down(0)
        return v
