import linkedList

list1 = linkedList.LinkedList([33, 56, 21, 99, 11])
list1.print_list()
print()

print("Insert 34 into the beginning: ")
list1.insert_beginning(34)
list1.print_list()
print()

print("Insert 222 into the end: ")
list1.insert_end(222)
list1.print_list()
print()

print("Insert 27, into index 5: ")
list1.insert_index(27, 5)
list1.print_list()
print()

print("Delete first: ")
list1.delete_first()
list1.print_list()
print()

print("Delete last: ")
list1.delete_last()
list1.print_list()
print()

print("Delete at index 3: ")
list1.delete_index(3)
list1.print_list()
print()

# Get middle of list and split
mid = list1.get_mid(list1.head)
sec_half = mid.next
mid.next = None

# Print first half
first_half = linkedList.LinkedList()
first_half.head = list1.head
print("First Half: ")
first_half.print_list()
print()

# Print second half
second_half = linkedList.LinkedList()
second_half.head = sec_half
print("Second Half: ")
second_half.print_list()
print()

# Sort each half independently
sort_first = first_half.merge_sort_list(first_half.head)
sort_second = second_half.merge_sort_list(second_half.head)

# Merge sorted halves
merged_list = list1.merge_lists(sort_first, sort_second)
list1.head = merged_list

print("Merged and sorted list:")
list1.print_list()