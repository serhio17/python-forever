# WARN: looks good, some fixes and improvements required. Also, I woluld like to introduce flake8 utility
# (https://habrahabr.ru/company/dataart/blog/318776/) it can be useful to check that PEP8 standard applied for code.

# TODO: please divide you code into functions for specific sub-tasks, please use `if __name == "__main__"` and call
# for main() function instead of flat code. Transfer your array to each function which will solve sub-task.
my_list = [91, 90, 92, -94, 93, -97, 96, 95, 99, 98]

# # Print only elements which are > 0
# # TODO: please print results with indexes, in this way:
# # Elements which are > 0:
# #     i[0] = 91
# #     i[1] = 90
# #     i[2] = 90
# #     i[4] = 93
print("Elements which are > 0:")
for i in range(0, len(my_list)):
    if my_list[i] > 0:
        print('i[{0}] = {1}'.format(i, my_list[i]))
print()

# Print only odd values of elements
print("Odd elements in the list:")
for i in my_list:
    if i % 2 == 1:
        print(i)
print()

# TODO: use enumerate instead of range
# Print elements which have even position in the list
print("Elements with even position:")
for i in enumerate(my_list):
    if i[1] % 2 == 0:
        print(i[1])
print()

# TODO: please do not use build in functions, provide you own algorithm to get maximum value
# Find a maximum element in the list
max_element = 0
for i, j in enumerate(my_list):
    if j > max_element:
        max_element = j
        index = i
print("The maximum element in the list is:")
print('i[{0}] = {1}'.format(index, my_list[index]))

# # TODO: please do not use build in functions, provide you own algorithm to get minimal value
# Find a minimum element in the list
min_element = 0
for i, j in enumerate(my_list):
    if j < min_element:
        min_element = j
        index = i
print("The minimum element in the list is:")
print('i[{0}] = {1}'.format(index, my_list[index]))
