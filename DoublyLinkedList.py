class Item:
    def __init__(self, value):
        self.prev = None
        self.value = value
        self.next = None


class DoublyLinkedList:
    """
    >>> dll1 = DoublyLinkedList()
    >>> dll1.insert(5)
    >>> dll1.insert(2)
    >>> dll1.insert(3)
    >>> dll1.insert(1)
    >>> dll1.delete(3)
    >>> dll1.insert(6)
    >>> dll1.delete(5)
    >>> dll1.show()
    6 1 2
    >>> dll2 = DoublyLinkedList()
    >>> dll2.insert(5)
    >>> dll2.insert(2)
    >>> dll2.insert(3)
    >>> dll2.insert(1)
    >>> dll2.delete(3)
    >>> dll2.insert(6)
    >>> dll2.delete(5)
    >>> dll2.deleteFirst()
    >>> dll2.deleteLast()
    >>> dll2.show()
    1
    """

    def __init__(self):
        self.head = Item("HEAD")
        self.tail = Item("TAIL")
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert(self, value):
        item = Item(value)
        item.next = self.head.next
        self.head.next = item
        item.next.prev = item
        item.prev = self.head

    def delete(self, value):
        tmp = self.head.next
        while tmp is not self.tail:
            if tmp.value == value:
                tmp.prev.next = tmp.next
                tmp.next.prev = tmp.prev
                return
            tmp = tmp.next

    def deleteFirst(self):
        tmp = self.head.next
        if tmp is not self.tail:
            self.head.next = tmp.next
            tmp.next.prev = self.head

    def deleteLast(self):
        tmp = self.tail.prev
        if tmp is not self.head:
            self.tail.prev = tmp.prev
            tmp.prev.next = self.tail

    def show(self):
        tmp = self.head.next
        result = ""
        while tmp is not self.tail:
            result = result + " " + str(tmp.value)
            tmp = tmp.next
        result = result[1:]
        print(result)

    def swap(self, swap_target_x, swap_target_y):
        # a - x - b - c(tmp_prev) - y - d(tmp_next)  を
        # a - y - b - c           - x - d            にする
        tmp_prev = swap_target_y.prev
        tmp_next = swap_target_y.next

        swap_target_x.prev.next = swap_target_y  # (a -> x)  =>  (a -> y)
        swap_target_x.next.prev = swap_target_y  # (x <- b)  =>  (y <- b)
        swap_target_y.prev = swap_target_x.prev  # (c <- y)  =>  (a <- y)
        swap_target_y.next = swap_target_x.next  # (y -> d)  =>  (y -> b)
        tmp_prev.next = swap_target_x            # (c -> y)  =>  (c -> x)
        tmp_next.prev = swap_target_x            # (y <- d)  =>  (x <- d)
        swap_target_x.prev = tmp_prev            # (a <- x)  =>  (c <- x)
        swap_target_x.next = tmp_next            # (x -> b)  =>  (x -> d)

        # xとyが隣り合っていたときの対策
        if swap_target_y.next is swap_target_y:
            swap_target_y.next = swap_target_x   # (y -> y)  =>  (y -> x)
            swap_target_x.prev = swap_target_y   # (x <- x)  =>  (y <- x)

    def insert_move(self, destination_prev, target):
        # a(destination_prev) - b - c - d(target) - e を
        # a                   - d - b - c         - d にする
        target.prev.next = target.next       # (c -> d)  =>  (c -> e)
        target.next.prev = target.prev       # (d <- e)  =>  (c <- e)
        target.next = destination_prev.next  # (d -> e)  =>  (d -> b)
        destination_prev.next.prev = target  # (a <- b)  =>  (d <- b)
        target.prev = destination_prev       # (c <- d)  =>  (a <- d)
        destination_prev.next = target       # (a -> b)  =>  (a -> d)


class DoubleDataDoublyLinkedList(DoublyLinkedList):
    """
    >>> dll3 = DoubleDataDoublyLinkedList()
    >>> dll3.insert("H4")
    >>> dll3.insert("C9")
    >>> dll3.insert("S4")
    >>> dll3.insert("D2")
    >>> dll3.insert("C3")
    >>> dll3.show()
    C3 D2 S4 C9 H4
    >>> dll4 = DoubleDataDoublyLinkedList()
    >>> dll4.insert("H4")
    >>> dll4.insert("C9")
    >>> dll4.insert("S4")
    >>> dll4.insert("D2")
    >>> dll4.insert("C3")
    >>> dll4.delete("D2")
    >>> dll4.delete("S4")
    >>> dll4.deleteFirst()
    >>> dll4.deleteLast()
    >>> dll4.show()
    C9
    """

    def insert(self, raw_input):
        picture = raw_input[0]
        value = int(raw_input[1])
        super(DoubleDataDoublyLinkedList, self).insert(value)
        self.head.next.picture = picture

    def delete(self, raw_input):
        picture = raw_input[0]
        value = int(raw_input[1])
        tmp = self.head.next
        while tmp is not self.tail:
            if tmp.value == value and tmp.picture == picture:
                tmp.prev.next = tmp.next
                tmp.next.prev = tmp.prev
                return
            tmp = tmp.next

    def show(self):
        tmp = self.head.next
        result = ""
        while tmp is not self.tail:
            result = result + " " + tmp.picture + str(tmp.value)
            tmp = tmp.next
        result = result[1:]
        print(result)

    def copy(self):
        dll_copy = DoubleDataDoublyLinkedList()
        original = self.tail.prev
        while original is not self.head:
            dll_copy.insert(original.picture + str(original.value))
            original = original.prev
        return dll_copy


if __name__ == "__main__":
    import doctest
    doctest.testmod()
