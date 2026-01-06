"""
Challenge: List Manipulation

1. Create a list with 5 numbers of your choice.
2. Display the first and last elements of the list.
3. Replace the second element with the value 100.
4. Add the number 200 to the end of the list.
5. Delete the third element from the list.
6. Display the final list.

"""


# Step 1: Create a list with 5 numbers of your choice.

numbers = [10, 20, 30, 40, 50]

# Step 2: Display the first and last elements of the list.
print("First element:", numbers[0])
print("Last element:", numbers[-1])

# Step 3: Replace the second element with the value 100.
numbers[1] = 100

# Step 4: Add the number 200 to the end of the list.
numbers.append(200)

# Step 5: Delete the third element from the list.
del numbers[2]

# Step 6: Display the final list.
print("Final list:", numbers)