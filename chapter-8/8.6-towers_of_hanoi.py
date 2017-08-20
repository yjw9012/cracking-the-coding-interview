
class TowersOfHanoi:

    def __init__(self, data):
        self.s1 = sorted(data, reverse=True)
        self.s2 = []
        self.s3 = []

    def moveToLastTower(self):
        self.move(len(self.s1), self.s1, self.s2, self.s3)

    def move(self, n, src, tmp, dest):
        if n == 1:
            dest.append(src.pop())
            return

        self.move(n-1, src, dest, tmp)
        self.move(1, src, tmp, dest)
        self.move(n-1, tmp, src, dest)


if __name__ == '__main__':

    disks = [1,2,3,4,5]
    hanoi = TowersOfHanoi(disks)

    assert hanoi.s1 == [5,4,3,2,1]
    assert not len(hanoi.s2)
    assert not len(hanoi.s3)

    hanoi.moveToLastTower()

    assert not len(hanoi.s1)
    assert not len(hanoi.s2)
    assert hanoi.s3 == [5,4,3,2,1]
