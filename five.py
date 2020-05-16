'''Given a singly-linked list, find the middle value in the list'''
from linkedlist import LinkedList

def middle_value(linked_list):
    size = 0
    node = linked_list.head
    while node is not None:
        size += 1
        node = node.next
    if size % 2 == 0:
        return None
    node = linked_list.head
    for _ in range(size // 2):
        node = node.next
    return node.data

'''Rotate a singly-linked list counterclockwise by k nodes, where k is a given integer'''

def rotate_links(linked_list, k):

    if linked_list.is_empty():
        return #return None

    for i in range(k):
        checking = linked_list.tail
        linked_list.delete(checking.data)
        linked_list.prepend(checking.data)
    return linked_list

argument_list = LinkedList(['A', 'B', 'C', 'D', 'E'])
rotation_list = LinkedList([4, 5, 6, 7])
k = 3

if __name__ == "__main__":
    print('middle value:')
    print(middle_value(argument_list))
    print('rotate:')
    print(rotate_links(rotation_list, 3))