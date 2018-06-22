from test_framework import generic_test


def merge_two_sorted_lists(L1, L2):
    # TODO - you fill in here.
    if l1 is None and l2 is None:
        return None
    elif l2 is None:
        return l1
    elif l1 is None:
        return l2
    else:
        head = tail = ListNode(0)
        while l1 and l2:
            if l1.val >= l2.val:
                tail.next = l2
                l2 = l2.next
            else:
                tail.next = l1
                l1 = l1.next
            tail = tail.next
    
        tail.next = l1 or l2 
        return head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_lists_merge.py",
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))