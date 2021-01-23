### Groups algorithm
### Version 0.1
"""Challenge:
Create an algorithm which randomly assigns a list of students to a group
The algorithm should maximise the number of people each person meets over several iterations"""

#Parameters:
#Students = 80
#Group size = 4

# @TODO Extend for 80 % 4 != 0

# Import packages
from random import choice, seed
from math import ceil
import names

# Set seed for reproducibility
set_seed = seed(42)

# Student list input [@TODO - add functionality to read from csv]
def student_list_generator(n):
    """ Generates a list of n names"""
    # Initialise student_list
    student_list = []
    for n in range(0,n):
        student_list.append(names.get_first_name())
    return student_list


data_science_class = student_list_generator(80)

#harrys_friends = ['Fred', 'George', 'Harry', 'Hermione', 'Ron', 'Ginny', 'Luna', 'Neville']

# Initialise a N dictionaries for each iteration (group_dict_N) [@TODO - create function]
#group_dict_1 = {}

########################################################################################################################
# BASIC FUNCTIONS
########################################################################################################################


def initialise_group_memory(people_list):
    """ A function that initialises the group memory dict and adds all people from a list as keys"""
    people_dict = {student: [] for student in people_list}  # Initialise group memory
    return people_dict


def initialise_group_dict(n):
    """ Initialises a group dictionary for n groups"""
    group_dict = {i : [] for i in range(1, n + 1)}
    return group_dict


def assign_group(group_dict, group_n, student, student_list):
    """ A function that adds a student to the group and removes them from the main list"""
    group_dict[group_n].append(student)
    student_list.remove(student)
#    print("{} added to group".format(student))
    return group_dict, student_list


def remember_group(group_dict, group, memory):
    """ A function that adds all members of a group to memory, along with the students they have worked with"""
    for student_i in group_dict[group]:
        for student_j in group_dict[group]:
            if student_i != student_j:
                memory[student_i].append(student_j)
    return memory

########################################################################################################################
# GROUP BUILDER FUNCTION
########################################################################################################################


# For a given number of iterations: [@TODO - Add functionality]
# Until the list of students is empty for the number of required groups (8 0 /4=20): [@TODO - Add functionality]


def form_group(group_dict, group_n, s_list, memory): #[@TODO - Add variables for group numbers and group size]
    # Ensure that the loop stops running if the list is empty
    # Create a loop that runs until the group size = 4
    while len(group_dict[group_n]) <= 4:
        if len(group_dict[group_n]) == 4:
            break
    # Randomly select a student from the copy list
        chosen_student = choice(s_list)
        print("Chosen student is {}".format(chosen_student))

        # Check 1 - Is the group empty?
        if len(group_dict[group_n]) == 0:
            # Add to the group
            group_dict, s_list = assign_group(group_dict, group_n, chosen_student, s_list)
#                print(group_dict)
#                print(type(group_dict))
        # Check 2 - Have they worked with an existing group member before
        elif len([student for student in group_dict[group_n] if student in memory[chosen_student]])>0: #[@TODO - fix elif]
            pass
            # If they have not worked with the chosen student, assign to a group
        else:
            group_dict, s_list = assign_group(group_dict, group_n, chosen_student, s_list)
#                print(group_dict)
        # Add all students in group to memory
    return group_dict, s_list

########################################################################################################################
# Populate n groups
########################################################################################################################


def populate_groups(s_list, memory):
    # Calculate number of groups required
    n_groups = ceil(len(s_list) / 4)
    print("{} groups required".format(n_groups))

    # Initialise group dictionary
    dictionary_of_groups = initialise_group_dict(n_groups)

    # Form groups
    for n in range(1, n_groups + 1):
        dictionary_of_groups, updated_student_list = form_group(dictionary_of_groups, n, s_list, memory)
        group_memory = remember_group(dictionary_of_groups, n, memory)
    return dictionary_of_groups, updated_student_list, group_memory



## 1. Initialise group memory
group_memory = initialise_group_memory(data_science_class)
#print(group_memory)

## 2. Initialise group dict
#dictionary_of_groups = initialise_group_dict(2)
#print(len(dictionary_of_groups[1]))

## 3. Populate groups
dictionary_of_groups, data_science_class_updated, group_memory = populate_groups(data_science_class, group_memory)

#print("Student list after group 1 {}".format(harrys_list_updated))
#print("Student list after group 2 {}".format(harrys_list_updated_2))
print("Dictionary of groups is \n{}".format(dictionary_of_groups))
print("Remaining students to be assigned: \n{}".format(data_science_class_updated))
print("Group memory is: \n{}".format(group_memory))

## 4. Remember group
#group_memory = remember_group(group_1, group_memory)

## 5. Return outcome
#print("Group is {}".format(group_1))
#print("Group memory is \n{}".format(group_memory))
#print("Updated student list is {}".format(harrys_list_updated))


# If the list is not currently empty
#    else:
    # Check if this student has worked with others already in the list, using memory dictionary
#        for value in group_dict_1['group_1'].values():
#            print(value)
#                pass
#            else:
#                group_dict_1['group_1'].append(chosen_student)
#                copy_student_list.remove(chosen_student)
#                print(copy_student_list)

#print(group_dict_1)

# Could potentially just merge dictionaries at the end of each iteration?
