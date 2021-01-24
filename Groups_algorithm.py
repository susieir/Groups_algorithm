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
import pandas as pd

# Set seed for reproducibility
set_seed = seed(42)

# Initialise student list
data_science_class = [i for i in range(1, 81)]

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
#        print("Chosen student is {}".format(chosen_student))

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
    copy_s_list = list(s_list)
    n_groups = ceil(len(copy_s_list) / 4)
#    print("{} groups required".format(n_groups))

    # Initialise group dictionary
    dictionary_of_groups = initialise_group_dict(n_groups)

    # For each group
    for n in range(1, n_groups + 1):
        # Populate group
        dictionary_of_groups, updated_student_list = form_group(dictionary_of_groups, n, copy_s_list, memory)
        # Remember group
        group_memory = remember_group(dictionary_of_groups, n, memory)
    return dictionary_of_groups, group_memory

def main(s_list, iter):
    """ A function that creates groups from a student list to maximise the number of students each other
    student meets over a specific number of iterations"""
    # Initialise memory
    s_mem = initialise_group_memory(s_list)
    print(s_mem)

    # Initialise list of group dictionaries for each iteration
    list_of_groups = []

    # Repeat group population for the required number of iterations
    for i in range(iter):
        # Populate groups
        dictionary_of_groups, memory = populate_groups(s_list, s_mem)
        # Add dictionary of groups to list of groups dictionary
        list_of_groups.append(dictionary_of_groups)
    return list_of_groups, memory



    ## 3. Populate groups
# Iteration 1
#dictionary_of_groups_iter1, group_memory = populate_groups(data_science_class, group_memory)

# Iteration 2
#dictionary_of_groups_iter2, group_memory = populate_groups(data_science_class, group_memory)


list_of_groups, group_memory = main(data_science_class, 2)
print(list_of_groups[0])
print(list_of_groups[1])
print(group_memory)

#list_of_groups_df.to_csv('list_of_groups_2.csv')

#print("Memory is \n{}".format(main(data_science_class, 3)[1]))


#print("Student list after group 1 {}".format(harrys_list_updated))
#print("Student list after group 2 {}".format(harrys_list_updated_2))
#print("Dictionary of groups iter 1 is \n{}".format(dictionary_of_groups_iter1))
#print("Dictionary of groups iter 2 is \n{}".format(dictionary_of_groups_iter2))
#print("Group memory is: \n{}".format(group_memory))

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
