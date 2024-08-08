my_array = [7, 12, 9, 4, 11]
print(my_array[0])

# Lowest value in the array

minVal = my_array[0]  # Step 1

for i in my_array:  # Step 2
    if i < minVal:  # Step 3
        minVal = i

print('Lowest value: ', minVal)  # Step 4
