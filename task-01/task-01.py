my_list=[91, 90, 92, -94, 93, -97, 96, 95, 99, 98]

# Print only elements which are > 0
print("Elements which are > 0:")
for i in my_list:
    if i > 0:
        print(i)
print()

# Print only odd values of elements
print("Odd elements in the list:")
for i in my_list:
    if i % 2 == 1:
        print(i)
print()

# Print elements which have even position in the list
print("Elements with even position:")
for i in range(0, len(my_list)):
    if i %2 == 0:
        print(my_list[i])
print()

print("The maximum element in the list is:")
print(max(my_list))
print()

print("The minimum element in the list is:")
print(min(my_list))
print()