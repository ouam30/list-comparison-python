"""
Python module which accepts any number of lists as parameters and returns:

Args:
    any number of lists
Returns:
    Strings that appear in more than one list
    The total number of unique strings across all lists
    The total number of strings that were processed

"""

def analyse_lists(*arg):
    """
    Analyses any number of lists and return the relevant information

    Args:
        Any number of lists
    Returns:
        Strings that appear in more than one list
        The total number of unique strings across all lists
        The total number of strings that were processed

    """
    # compare all lists
    strings_in_multiple_list = compare_lists(*arg)

    # function to return nb of unique items
    unique_strings_count = number_of_unique_strings(*arg)

    # function to return total number of items
    strings_processed_count = number_of_strings_processed(*arg)

    return ','.join(strings_in_multiple_list), unique_strings_count, strings_processed_count


def compare_lists(*arg):
    """Compares any number of lists and return all strings that appear in more than one list"""

    strings_in_multiple_list = []
    # function to find items in multiple lists
    for index, list1 in enumerate(arg):
        for list2 in arg[index + 1:]:
            duplicate_items = find_duplicates(list1, list2)
            if duplicate_items:
                strings_in_multiple_list.append(','.join(duplicate_items))

    return strings_in_multiple_list


def number_of_unique_strings(*arg):
    """Goes through all lists and return the number of unique strings"""

    master_list = []
    for _list in arg:
        master_list = master_list + _list

    return len(set(master_list))


def number_of_strings_processed(*arg):
    """Goes through all lists and return the number of all strings processed"""

    strings_processed_count = 0
    for _list in arg:
        strings_processed_count = strings_processed_count + len(_list)

    return strings_processed_count


def find_duplicates(list1, list2):
    """Compare items in 2 lists and return the list of items present in both

    Args:
        list1: the list which will be iterated through to check if the item are present in list2
        list2: the list of items which will be compared to list1
    Returns:
        a list containing all strings present in both lists

    >>> find_duplicates(['g', 'gh', 'ghj' ,'g'], ['j', 'ju', 'gh', 'gk', 'gn'])
    ['gh']

    The function will still work with empty lists or sets

    >>> find_duplicates([], ['j', 'ju', 'gh', 'gk', 'gn'])
    []

    >>> find_duplicates(['g', 'gh', 'ghj' ,'g'], [])
    []

    >>> find_duplicates({'g', 'gh', 'ghj' ,'g'}, {'j', 'ju', 'gh', 'gk', 'gn'})
    ['gh']

    """

    duplicate_items_list = []

    # print('comparing {} with {}'.format(list1, list2))
    for item in list1:
        if item in list2:
            duplicate_items_list.append(item)

    return duplicate_items_list


def main():
    """main function which returns all the relevant data"""

    list_1 = ['g', 'gh', 'ghj', 'g']
    list_2 = ['j', 'ju', 'gh', 'gk', 'gn']
    # list3 = ['y', 'h', 'rg' ,'gn']

    strings_in_multiple_list, unique_strings_count, strings_processed_count = analyse_lists(list_1,
                                                                                            list_2)
    #strings_in_multiple_list, unique_strings_count, strings_processed_count = analyse_lists(list1,
    #                                                                                        list2,
    #                                                                                        list3)

    print('Strings appearing in multiple lists: {}'.format(strings_in_multiple_list))
    print('Number of unique strings: {}'.format(str(unique_strings_count)))
    print('Total number of strings processed: {}'.format(str(strings_processed_count)))


if __name__ == "__main__":
    main()
