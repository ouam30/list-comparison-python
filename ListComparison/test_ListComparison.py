import pytest

from ListComparison import *


def test_analyse_2_lists():
    list1 = ['g', 'gh', 'ghj' ,'g']
    list2 = ['j', 'ju', 'gh', 'gk', 'gn']
    assert analyse_lists(list1, list2) == ('gh', 7, 9)
    
    
def test_analyse_2_lists_2():
    list1 = ['g', 'gh', 'ghj']
    list2 = ['j', 'ju', 'gh', 'gk', 'gn', 'g']
    assert analyse_lists(list1, list2) == ('g,gh', 7, 9)
    
    
def test_analyse_3_lists():
    list1 = ['g', 'gh', 'ghj', 'g']
    list2 = ['j', 'ju', 'gh', 'gk', 'gn']
    list3 = ['y', 'h', 'rg', 'gn']
    assert analyse_lists(list1, list2, list3) == ('gh,gn', 10, 13)
    
    
def test_number_of_strings_processed():
    list1 = ['g', 'gh', 'ghj' ,'g']
    list2 = ['j', 'ju', 'gh', 'gk', 'gn']
    assert number_of_strings_processed(list1, list2) == 9


def test_number_of_unique_strings():
    list1 = ['g', 'gh', 'ghj' ,'g']
    list2 = ['j', 'ju', 'gh', 'gk', 'gn']
    assert number_of_unique_strings(list1, list2) == 7


def test_find_duplicates_two_lists():
    list1 = ['g', 'gh', 'ghj' ,'g']
    list2 = ['j', 'ju', 'gh', 'gk', 'gn']
    assert find_duplicates(list1, list2) == ['gh']


def test_compare_two_lists():
    list1 = ['g', 'gh', 'ghj' ,'g']
    list2 = ['j', 'ju', 'gh', 'gk', 'gn']
    assert compare_lists(list1, list2) == ['gh']


def test_duplicate_item_in_one_list_is_not_counted():
    list1 = ['g', 'gh', 'ghj' ,'g']
    list2 = ['j', 'ju', 'gk', 'gn']
    assert len(compare_lists(list1, list2)) == 0


def test_compare_three_lists():
    list1 = ['g', 'gh', 'ghj' ,'g']
    list2 = ['j', 'ju', 'gh', 'gk', 'gn']
    list3 = ['y', 'h', 'rg' ,'gn']
    assert compare_lists(list1, list2, list3) == ['gh','gn']


def test_find_duplicates_list1_empty():
    list1 = []
    list2 = ['j', 'ju', 'gh', 'gk', 'gn']
    assert find_duplicates(list1, list2) == []


def test_find_duplicates_list2_empty():
    list1 = ['g', 'gh', 'ghj' ,'g']
    list2 = []
    assert find_duplicates(list1, list2) == []


def test_find_duplicates_two_sets():
    list1 = {'g', 'gh', 'ghj' ,'g'}
    list2 = {'j', 'ju', 'gh', 'gk', 'gn'}
    assert find_duplicates(list1, list2) == ['gh']

