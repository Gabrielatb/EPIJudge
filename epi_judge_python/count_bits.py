from test_framework import generic_test


def count_bits(x):
    # TODO - you fill in here.
    #return 0

    num_bits = 1
    while x:
        num_bits += x & 1
        x>= 1

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("count_bits.py", 'count_bits.tsv',
                                       count_bits))
