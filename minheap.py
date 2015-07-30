from exceptions import HeapEmptyError


class HeapElement(object):
    def __init__(self, char=None, count=0, left=None, right=None):
        self.char = char
        self.count = count
        self.left = left
        self.right = right

    def serialize(self):
        pass

    def generate_mappings(self, dictionary, code=''):
        if self.char:
            dictionary.update({self.char: code})
        else:
            if self.left:
                self.left.generate_mappings(dictionary, code + '0')
            if self.right:
                self.right.generate_mappings(dictionary, code + '1')

    def __lt__(self, other):
        return self.count < other.count

    def __le__(self, other):
        return self.count <= other.count

    def __gt__(self, other):
        return self.count > other.count

    def __ge__(self, other):
        return self.count >= other.count

    def __str__(self):
        return '("%s": %d)' % (self.char, self.count)


class MinHeap(object):
    def __init__(self):
        self.heap = []

    def _sift_down(self, index):
        left = index * 2 + 1
        while left < len(self.heap):
            min_index = index
            if self.heap[left] < self.heap[min_index]:
                min_index = left
            right = index * 2 + 2
            if right < len(self.heap) and self.heap[right] < self.heap[min_index]:
                min_index = right
            if min_index != index:
                self.swap(index, min_index)
                index = min_index
                left = index * 2 + 1
            else:
                break

    def _sift_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[index] < self.heap[parent]:
                self.swap(index, parent)
                index = parent
            else:
                break

    def size(self):
        return len(self.heap)

    def empty(self):
        return bool(self.size())

    def swap(self, index1, index2):
        tmp = self.heap[index1]
        self.heap[index1] = self.heap[index2]
        self.heap[index2] = tmp

    def push(self, element):
        self.heap.append(element)
        self._sift_up(self.size() - 1)

    def top(self):
        try:
            return self.heap[0]
        except IndexError:
            raise HeapEmptyError('Cannot access top element because heap is empty')

    def pop(self):
        try:
            self.heap[0] = self.heap[-1]
            del self.heap[-1]
            self._sift_down(0)
        except IndexError:
            raise HeapEmptyError('Cannot pop element because heap is empty')

    def merge(self):
        element1 = self.top()
        self.pop()
        element2 = self.top()
        self.pop()
        new_element = HeapElement(count=element1.count + element2.count, left=element1, right=element2)
        self.push(new_element)

    def merge_to_single_element(self):
        if self.size() > 1:
            while self.size() > 1:
                self.merge()
        elif self.size() == 1:
            element = self.top()
            self.pop()
            new_element = HeapElement(count=element.count, left=element)
            self.push(new_element)
        else:
            new_element = HeapElement(count=0)
            self.push(new_element)
        return self.top()

    @classmethod
    def build_from_dict(cls, dictionary):
        heap = cls()
        for char, count in dictionary.items():
            heap.push(HeapElement(char=char, count=count))
        return heap

    def __str__(self):
        return '\n'.join((str(element) for element in self.heap))