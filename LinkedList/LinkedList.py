# get_head() - returns the head of the list
# insert_at_tail(data) - inserts an element at the end of the linked list
# insert_at_head(data) - inserts an element at the start/head of the linked list
# delete(data) - deletes an element with your specified value from the linked list
# delete_at_head() - deletes the first element of the list
# search(data) - searches for an element with the specified value in the linked list
# is_empty() - returns true if the linked list is empty
from Node import Node


class LinkedList:
    def __init__(self) -> None:
        self.head_node = None

    def insert_at_head(self, data):
        temp_node = Node(data)
        temp_node.next_element = self.head_node
        self.head_node = temp_node
        return self.head_node

    def get_head(self):
        return self.head_node

    def insert_at_tail(lst, value):
        new_node = Node(value)
        if lst.get_head() is None:
            lst.head_node = new_node
            return
        temp = lst.get_head()
        while temp.next_element:
            temp = temp.next_element
        temp.next_element = new_node
        return

    def is_empty(self):
        if self.head_node is None:
            return True
        else:
            return False

    def print_list(self):
        if self.is_empty():
            print("Linked List is empty")
            return False
        temp = self.head_node
        while temp.next_element is not None:
            print(temp.data, end=" -> ")
            temp = temp.next_element
        print(temp.data, end=" None ")
        return True


lst = LinkedList()
print(lst.get_head())
print(lst.is_empty())
lst.print_list()

print("inserting values in the list")
for i in range(1, 10):
    lst.insert_at_head(i)
print(lst.print_list())
