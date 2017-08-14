from Node import Node

# if the digits are stored in forward order:
def sum_lists(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    lis1, lis2 = add_zero_nodes(head1, head2)
    result, carryover = sum_lists_recur(lis1, lis2)
    if carryover:
        result = Node(1, result)
    return result

def sum_lists_recur(head1, head2):
    if head1 is None:
        return None, 0

    subresult, carryover = sum_lists_recur(head1.next, head2.next)
    add_result = head1.data + head2.data + carryover
    carryover = 1 if add_result >= 10 else 0
    new_node = Node(add_result % 10, subresult)
    return new_node, carryover


def add_zero_nodes(head1, head2):
    len1 = len(head1)
    len2 = len(head2)
    diff = abs(len1 - len2)
    short_list, long_list = head1, head2
    if diff >= 1:
        short_list = head1 if len1 < len2 else head2
        long_list = head1 if short_list is head2 else head2
        for i in range(diff):
            new_head = Node(0, short_list)
            short_list = new_head
    return short_list, long_list


node1 = Node(6)
node2 = Node(1)
node3 = Node(7)
node1.next = node2
node2.next = node3

node4 = Node(2)
node5 = Node(9)
node6 = Node(5)
node4.next = node5
node5.next = node6

# Should be 9 -> 1 -> 2
sum_lists(node1, node4).print_node_list()

node4.data = 5
# Should be 1 -> 2 -> 1 -> 2
sum_lists(node1, node4).print_node_list()

node4.next = Node(3, node4.next)
# Should be 6 -> 0 -> 1 -> 2
sum_lists(node1, node4).print_node_list()
