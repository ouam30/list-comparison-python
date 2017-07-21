
def compare_lists(list1, list2, list3):
    
    lists = [list1, list2, list3]

    strings_in_multiple_list = []
    unique_strings_count = 0
    strings_processed_count = 0
    master_list = []

    for index, list1 in enumerate(lists):
        strings_processed_count = strings_processed_count + len(list1)
        master_list = master_list + list1
        for list2 in lists[index + 1:]:
            #print('comparing {} with {}'.format(list1, list2))
            for item in list1:
                if item in list2:
                    strings_in_multiple_list.append(item)

    unique_strings_count = len(set(master_list))
    output_data(set(strings_in_multiple_list), unique_strings_count, strings_processed_count)


def output_data(strings_in_multiple_list, unique_strings_count, strings_processed_count):
    print('Strings appearing in multiple lists: {}'.format(', '.join(strings_in_multiple_list)))
    print('Number of unique strings: {}'.format(str(unique_strings_count)))
    print('Total number of strings processed: {}'.format(str(strings_processed_count)))

