from test_framework import generic_test


def reverse_sublist(L, start, finish):
    # TODO - you fill in here.

    #not clean version, version #1
    while head is None:
    return None
    
    dummy_head = tail = ListNode(0)
    count = 0
    while m-1 > count:
        count += 1
        tail.next = head
        tail = tail.next
        head = head.next
       
    to_new_head = head
    rev_tail = head
    for _ in range(m,n):
        rev_tail = rev_tail.next
        head = head.next
    head = head.next

    rev_tail.next = None
    
    new_head = self.reverse(to_new_head)
    tail.next = new_head
    while tail.next:
        tail = tail.next
    
    tail.next = head
    
    return dummy_head.next
    


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_sublist.py",
                                       "reverse_sublist.tsv", reverse_sublist))
