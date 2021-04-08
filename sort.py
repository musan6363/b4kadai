import DoublyLinkedList as dll


def insertion_sort(data):
    """
    >>> data1 = dll.DoublyLinkedList()
    >>> data1.insert(3)
    >>> data1.insert(1)
    >>> data1.insert(6)
    >>> data1.insert(4)
    >>> data1.insert(2)
    >>> data1.insert(5)
    >>> insertion_sort(data1)
    insertion sort
    5 2 4 6 1 3
    2 5 4 6 1 3
    2 4 5 6 1 3
    2 4 5 6 1 3
    1 2 4 5 6 3
    1 2 3 4 5 6
    >>> data2 = [5,2,4,6,1,3]
    >>> insertion_sort(data2)
    insertion sort
    [5, 2, 4, 6, 1, 3]
    [2, 5, 4, 6, 1, 3]
    [2, 4, 5, 6, 1, 3]
    [2, 4, 5, 6, 1, 3]
    [1, 2, 4, 5, 6, 3]
    [1, 2, 3, 4, 5, 6]
    """
    print("insertion sort")
    if type(data) is dll.DoublyLinkedList:
        data.show()
        target = data.head.next.next
        while target is not data.tail:
            sorted = target.prev
            while sorted is not data.head and sorted.x > target.x:
                sorted = sorted.prev
            new_target = target.next  # 次のtargetはtargetの次．上書きされないように保持
            # ここから 挿入処理 sortedの後ろにtargetを挿入
            target.prev.next = target.next
            target.next.prev = target.prev
            target.next = sorted.next
            target.prev = sorted
            sorted.next.prev = target
            sorted.next = target
            # ここまで 挿入処理
            target = new_target
            data.show()
    else:
        print(data)
        for i in range(1, len(data)):
            target = data[i]
            j = i - 1
            while j >= 0 and data[j] > target:
                data[j+1] = data[j]
                j -= 1
            data[j+1] = target
            print(data)


def bubble_sort(data):
    """
    >>> data1 = dll.DoublyLinkedList()
    >>> data1.insert(1)
    >>> data1.insert(4)
    >>> data1.insert(2)
    >>> data1.insert(3)
    >>> data1.insert(5)
    >>> bubble_sort(data1)
    bubble sort
    1 2 3 4 5
    8
    >>> data2 = [5,2,4,6,1,3]
    >>> bubble_sort(data2)
    bubble sort
    [1, 2, 3, 4, 5, 6]
    9
    """
    print("bubble sort")
    if type(data) is dll.DoublyLinkedList:
        count = 0
        flag = True
        unsorted_top = data.head.next
        while flag:
            flag = False
            target = data.tail.prev
            while target is not unsorted_top:
                if target.prev.x > target.x:
                    unsorted_top_prev = unsorted_top.prev  # 上書き防止
                    # ここから 入替処理
                    tmp_prev = target.prev.prev
                    tmp_next = target.prev
                    target.prev.prev.next = target
                    target.prev.prev = target
                    target.prev.next = target.next
                    target.next.prev = target.prev
                    target.prev = tmp_prev
                    target.next = tmp_next
                    # ここまで 入替処理
                    unsorted_top = unsorted_top_prev.next
                    flag = True
                    count += 1
                else:
                    target = target.prev
            unsorted_top = unsorted_top.next
        data.show()
        print(count)
    else:
        count = 0
        flag = True
        i = 1
        while flag:
            flag = False
            for j in range(len(data)-i):
                j = len(data) - j - 1  # N-1 ~ i+1
                if data[j] < data[j-1]:
                    tmp = data[j]
                    data[j] = data[j-1]
                    data[j-1] = tmp
                    flag = True
                    count += 1
            i += 1
        print(data)
        print(count)


def selection_sort(data):
    """
    >>> data1 = dll.DoublyLinkedList()
    >>> data1.insert(3)
    >>> data1.insert(1)
    >>> data1.insert(2)
    >>> data1.insert(4)
    >>> data1.insert(6)
    >>> data1.insert(5)
    >>> selection_sort(data1)
    selection sort
    1 2 3 4 5 6
    4
    >>> data2 = [5,6,4,2,1,3]
    >>> selection_sort(data2)
    selection sort
    [1, 2, 3, 4, 5, 6]
    4
    """
    print("selection sort")
    if type(data) is dll.DoublyLinkedList:
        count = 0
        unsorted_top = data.head.next
        while unsorted_top is not data.tail:
            count_flag = False
            min = unsorted_top
            target = unsorted_top.next
            while target is not data.tail:
                if target.x < min.x:
                    min = target
                    count_flag = True
                target = target.next
            # ここから minとunsorted_topの交換
            tmp_prev = min.prev
            tmp_next = min.next
            unsorted_top.prev.next = min
            unsorted_top.next.prev = min
            min.prev = unsorted_top.prev
            min.next = unsorted_top.next
            tmp_prev.next = unsorted_top
            tmp_next.prev = unsorted_top
            unsorted_top.prev = tmp_prev
            unsorted_top.next = tmp_next
            if min.next is min:
                # minとunsorted_topが隣り合っていたときの対策
                min.next = unsorted_top
                unsorted_top.prev = min
            # ここまで minとunsorted_topの交換
            unsorted_top = min.next
            if count_flag:
                count += 1
        data.show()
        print(count)
    else:
        count = 0
        for i in range(len(data)):
            count_flag = False
            minj = i
            for j in range(i, len(data)):
                if data[j] < data[minj]:
                    minj = j
                    count_flag = True
            tmp = data[i]
            data[i] = data[minj]
            data[minj] = tmp
            if count_flag:
                count += 1
        print(data)
        print(count)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
