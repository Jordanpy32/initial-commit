"""
Challenge: List Manipulation

1. Ask a user to enter 5 number (one by one) and stocke them in list
2. Display
   - The list
   - The maximum munber
   - The minimum number
   - The average of numbers
3. Display how many numbers are above average

input(), int(), len(), sum(), max(), min(), boucles for

"""
# creating my list
my_list = []

# loop to ask 5 numbers
for n in range(5):
    number = int(input("Enter a number : "))
    my_list.append(number) # add number to my list

# display my list
print("my_list = ",my_list)

max_number = max(my_list) # find the maximun number of my list
min_number = min(my_list) # find the minimun number of my list

# display the max and min number of my list
print(f"The max number = {max_number} and the min number = {min_number}")

list_average = sum(my_list) / len(my_list) # calculate the average of my list

# display the average of my list
print("list_average = ",list_average)

count_above_avg = 0
for number in my_list:
    if number > list_average: # compare each elements of my to the average
        count_above_avg +=1   # count the number of items greater than my list 

# disply number of elements above average of my list
print(f"number of elements above average is {count_above_avg}")