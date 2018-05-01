# WARN: looks good, some fixes and improvements required. Also, I woluld like to introduce flake8 utility
# (https://habrahabr.ru/company/dataart/blog/318776/) it can be useful to check that PEP8 standard applied for code.

# for main() function instead of flat code. Transfer your array to each function which will solve sub-task.


def elements_more_zero(my_list):
    print("Elements which are > 0:")
    for index, value in enumerate(my_list):
        if value > 0:
            print('i[{0}] = {1}'.format(index, value))
    print()


def elements_odd_values(my_list):
    # Print only odd values of elements
    print("Odd elements in the list:")
    for index, value in enumerate(my_list):
        if value % 2 == 1:
            print('i[{0}] = {1}'.format(index, value))
    print()


def elements_even_position(my_list):
    # Print elements which have even position in the list
    print("Elements with even position:")
    for index, value in enumerate(my_list):
        if index % 2 == 0:
            print('i[{0}] = {1}'.format(index, value))
    print()


def max_element(my_list):
    # Find a maximum element in the list
    max_element = None
    max_index = None
    for index, value in enumerate(my_list):
        if (max_element is None) or (value > max_element):
            max_element = value
            max_index = index

    print("The maximum element in the list is:")
    print('i[{0}] = {1}'.format(max_index, max_element))


def min_element(my_list):
    # # TODO: please do not use build in functions, provide you own algorithm to get minimal value
    # Find a minimum element in the list
    min_element = 0
    for i, j in enumerate(my_list):
        if j < min_element:
            min_element = j
            index = i
    print("The minimum element in the list is:")
    print('i[{0}] = {1}'.format(index, my_list[index]))


my_list = [91, 90, 92, -94, 93, -97, 96, 95, 99, 98]

elements_more_zero(my_list)
elements_odd_values(my_list)
elements_even_position(my_list)
max_element(my_list)
min_element(my_list)
