from Node import Node
from random import randint

class RandomNode(Node):

    def __init__(self, data, left=None, right=None):
        super().__init__(data, left, right)
        self.size = 1

class Tree:

    def __init__(self, data):
        self.root = RandomNode(data)

    def find(self, num):
        return find_recur(self.root, num)

    def find_recur(self, cur, num):
        if cur is None:
            return False
        if cur.data == num:
            return True
        return self.find_recur(cur.left, num) or self.find_recur(cur.right, num)

    def insert(self, num):
        if self.root is None:
            self.root = RandomNode(num)
        else:
            self.insert_recur(self.root, num)

    def insert_recur(self, cur, num):
        cur.size += 1
        if num <= cur.data:
            if cur.left is None:
                cur.left = RandomNode(num)
            else:
                self.insert_recur(cur.left, num)
        else:
            if cur.right is None:
                cur.right = RandomNode(num)
            else:
                self.insert_recur(cur.right, num)

    def get_random_node(self):
        return self.get_random_node_recur(self.root)

    def get_random_node_recur(self, cur):
        random_int = randint(1, cur.size)
        if random_int == 1:
            return cur
        elif cur.left is not None and random_int <= 1 + cur.left.size:
            return self.get_random_node_recur(cur.left)
        else:
            return self.get_random_node_recur(cur.right)


if __name__ == '__main__':

    tree = Tree(10)

    tree.insert(5)
    tree.insert(4)
    tree.insert(6)

    tree.insert(11)
    tree.insert(13)
    tree.insert(12)
    tree.insert(15)

    assert tree.find(5)
    assert tree.find(13)
    assert tree.find(12)
    assert tree.find(4)
    assert tree.find(10)

    assert not tree.find(0)

    print(tree.get_random_node().data)
