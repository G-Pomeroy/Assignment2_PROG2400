class LinkedList:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self, values=None):
        self.head = None
        self.tail = None
        self.size = 0

        if values is not None:
            for value in values:
                self.insert_end(value)

    def insert_beginning(self, value):
        new_node = self.Node(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_end(self, value):
        new_node = self.Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def insert_index(self, value, position):
        new_node = self.Node(value)
        current_node = self.head
        if position == 0:
            self.insert_beginning(value)
            return
        for x in range(position - 1):
            if current_node is None:
                print("Position out of bounds")
                return
            current_node = current_node.next
        new_node.next = current_node.next
        current_node.next = new_node

    def delete_first(self):
        if self.head:
            self.head = self.head.next

    def delete_last(self):
        if not self.head:
            return
        if self.head.next is None:
            self.head = None
            return
        second_last = self.head
        while second_last.next.next:
            second_last = second_last.next
        second_last.next = None

    def delete_index(self, position):
        if position == 0:
            self.delete_first()
            return
        current_node = self.head
        for x in range(position - 1):
            if current_node is None or current_node.next is None:
                print("Position out of bounds")
                return
            current_node = current_node.next
        if current_node.next is None:
            print("Position out of bounds")
            return
        current_node.next = current_node.next.next

    def merge_sort_list(self, start_node):
        if not start_node or not start_node.next:
            return start_node

        # Split the list into two halves
        mid = self.get_mid(start_node)
        second_half = mid.next
        mid.next = None

        # Recursively sort both halves
        sorted_first_half = self.merge_sort_list(start_node)
        sorted_second_half = self.merge_sort_list(second_half)

        # Merge the sorted halves
        return self.merge_lists(sorted_first_half, sorted_second_half)

    def merge_lists(self, list_a, list_b):
        dummy = LinkedList.Node(0)
        tail = dummy

        while list_a and list_b:
            if list_a.value <= list_b.value:
                tail.next = list_a
                list_a = list_a.next
            else:
                tail.next = list_b
                list_b = list_b.next
            tail = tail.next

        tail.next = list_a if list_a else list_b
        return dummy.next

    def get_mid(self, start_node):
        if not start_node:
            return None

        # Establish pointers
        slow_ptr = start_node
        fast_ptr = start_node

        # Slow pointer goes one by one, fast pointer goes in twos, slow_ptr will find mid when fast_ptr reaches end
        # of list
        while fast_ptr.next and fast_ptr.next.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        return slow_ptr

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.value, end=" ")
            current_node = current_node.next
        print()