#Python list lesson

#Lists are just about what you'd think they'd be. They just hold a list of
#values inside of them. In a way it's simppler than ditionaries. But interacting with
#them is much more complicated

my_list = [1,2,3,4,5]
print("Original list: ",my_list)
list_two = ["a","b","c","d","e"]
print(my_list)

#accessing the elements
#use square brackets alongside the chosen list to grab the specific item from the numbered index
#Of cousr the beginning index number is always 0. Just like most programs in general

print("Element at index 0: ", my_list[0])
print("Element at index 2: ", my_list[2])

#slicing
#slicing allows you to grab a specific section of the list
#in this example. we are slicing out just the first indexed value and taking the remaining 4
#... expect it isn't cause this shit is weird sometimes and what's actually happening is that
#It's using the values from the staring index and stopping at the end index. Leaving us with
#printing 1,2, and 3. Skipping 0. and ignoring 4. printng 2,3,4 in the end. As 1 is the starting
#index thus isn't skipped. and ending at 4 in which it will stop and not print 5. still skips 0

subset = my_list[1:4]
print(subset)
other_sub = list_two[1:4]
print(other_sub)

#modifying lists
my_list[2] = 10
print("modded list: ", my_list)

#adding to lists
my_list.append(6)
print("list after adding a new piece: ", my_list)

#removing from lists
my_list.remove(4)
print("List after removal of an item: ", my_list)

#List operations

#printing the length of the list

length = len(my_list)
print("Current length of my_list; ", my_list)

#concatenating
new_list = my_list + [7,8,9]
print("concatenated list: ", new_list)

#repeating elements
repeated_list = my_list * 2
print("repeating list: ",repeated_list)


#common methods of lists

#   .append adds an element to the end of the list
my_list.append(5)
print("list after appending: ", my_list)

count_of_five = my_list.count(5)
print("print of 5 in the list: ", count_of_five)

index_of_three = my_list.index(6)
print("Index of the value 6 in the list: ", index_of_three)