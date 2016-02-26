"""
Working with Lists
"""
my_list = [1, 2]

"""
Lists can be extended
"""
my_list.extend([3, 4])
assert my_list == [1, 2, 3, 4]

"""
Lists can be added using + operator
"""
other_list = [0, 0] + [1, 1]
assert other_list == [0, 0, 1, 1]

"""
We can add an item to a list using the
insert method
"""
my_list.insert(0, 0)
assert my_list == [0, 1, 2, 3, 4]

"""
We can get the length of a list using
the len function
"""
assert len(my_list) == 5

"""
List can be multiplied
"""
assert ['a'] * 2 == ['a', 'a']

"""
We can search for items in lists using
the in keyword
"""
assert 1 in [0, 2, 1]

"""
We can get the items of a list using
positive and negatives values
"""
assert [1, 2, 3, 4][0] == 1
assert [1, 2, 3, 4][-1] == 4

"""
We can get a set of items using :
"""
test_list = [1, 2, 3, 4]
assert test_list[0:] == test_list
assert test_list[1:3] == [2, 3]

"""
We can retrieve the index of a
given element within a list
"""
assert [1, 2, 3, 4].index(1) == 0
