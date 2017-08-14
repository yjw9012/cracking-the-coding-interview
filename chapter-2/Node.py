class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def print_node_list(self):
        cur = self
        node_list = []
        while cur is not None:
            node_list.append(str(cur.data))
            cur = cur.next
        print(" -> ".join(node_list))
