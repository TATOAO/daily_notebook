

# 一个特殊的完全二叉树 , 保证父节点大于子节点

class my_priority_queue():


    def __init__(self, cap:int):
        """
        假设固定一个capacity 最大长度
        """

        self.pq = [None] * (cap + 1)
        self.size = 0

    def max(self):
        return self.pq[1]

    def insert(self, e) -> None:
        """
        插入元素 e
        """
        ...

    def delMax(self):
        """
        删除并返回当前队列中最大元素
        """
        ...

    def swim(self, x: int) -> None:
        """
        上浮第 x 个元素，以维护最大堆性质
        """
        ...

    def sink(self, x: int) -> None:
        """
        下沉第 x 个元素，以维护最大堆性质
        """
        ...

    def swap(self, i: int, j: int) -> None:
        """
        交换数组的两个元素
        """
        temp = self.pq[i]
        self.pq[i] = self.pq[j]
        self.pq[j] = temp

    def less(self, i: int, j: int) -> bool:
        """
        pq[i] 是否比 pq[j] 小？
        """
        if self.pq[i] == None or self.pq[j] == None:
            return True
        else:
            return self.pq[i] <= self.pq[j]

    def left(self, index: int) -> int:
        """
        还有 left 三个方法
        """
        return index * 2

    def right(self, index: int) -> int:
        return index * 2 + 1

    def parent(self, index: int) -> int:
        return index // 2
