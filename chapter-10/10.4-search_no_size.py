class Listy:
    def __init__(self):
        self.arr = []

    def elementAt(self, i):
        try:
            elem = self.arr[i]
            return elem
        except:
            return -1

    def append(self, elem):
        self.arr.append(elem)


def search(listy, x):
    range_end = 1
    while listy.elementAt(range_end) != -1 and listy.elementAt(range_end) < x :
        range_end *= 2
    return binary_search(listy, x, range_end // 2, range_end)


def binary_search(listy, x, start, end):

    while start <= end:
        mid = (start + end) // 2
        if listy.elementAt(mid) == -1:
            end = mid - 1
        elif listy.elementAt(mid) == x:
            return mid
        elif listy.elementAt(mid) < x:
            start = mid + 1
        else:
            end = mid - 1

    return -1


if __name__ == '__main__':

    l = Listy()
    l.append(1)
    l.append(2)
    l.append(3)
    l.append(4)
    l.append(5)
    l.append(6)
    l.append(7)
    l.append(8)
    l.append(9)
    l.append(10)

    assert search(l, 6) == 5
    assert search(l, 11) == -1
