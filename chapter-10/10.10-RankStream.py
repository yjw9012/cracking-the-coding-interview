class RankStream:

    class Node:
        def __init__(self, data, rel_rank=0, left=None, right=None):
            self.data = data
            self.rel_rank = rel_rank
            self.left = left
            self.right = right

        def __str__(self):
            return str((self.data, self.rel_rank))

    def __init__(self, root_data):
        self.root = self.Node(root_data)

    def track(self, data):
        self.track_recur(self.root, data)

    def track_recur(self, cur, data):
        if cur.data == data:
            cur.rel_rank += 1
            return

        if data < cur.data:
            cur.rel_rank += 1
            if cur.left is None:
                cur.left = self.Node(data, 0)
            else:
                self.track_recur(cur.left, data)

        else:
            if cur.right is None:
                cur.right = self.Node(data, 0)
            else:
                self.track_recur(cur.right, data)

    def get_rank(self, data):
        return self.get_rank_recur(self.root, data, 0)

    def get_rank_recur(self, cur, data, rank_sum):
        if cur is None:
            return -1

        if cur.data == data:
            return rank_sum + cur.rel_rank

        if data < cur.data:
            return self.get_rank_recur(cur.left, data, rank_sum)
        else:
            return self.get_rank_recur(cur.right, data, rank_sum + cur.rel_rank + 1)

    def traverse(self):
        self.in_order(self.root)

    def in_order(self, cur):
        if cur is None:
            return

        self.in_order(cur.left)
        print(cur)
        self.in_order(cur.right)

if __name__ == '__main__':

    rank_stream = RankStream(5)
    rank_stream.track(1)
    rank_stream.track(4)
    rank_stream.track(4)
    rank_stream.track(5)
    rank_stream.track(9)
    rank_stream.track(7)
    rank_stream.track(13)
    rank_stream.track(3)

    rank_stream.traverse()

    assert rank_stream.get_rank(1) == 0
    assert rank_stream.get_rank(3) == 1
    assert rank_stream.get_rank(4) == 3
    assert rank_stream.get_rank(5) == 5
    assert rank_stream.get_rank(7) == 6
    assert rank_stream.get_rank(9) == 7
    assert rank_stream.get_rank(13) == 8
    assert rank_stream.get_rank(10) == -1
