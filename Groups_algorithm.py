"""                                     Groups algorithm                                                            """

# Version 0.1
"""Challenge:
Create an algorithm which randomly assigns a list of students to a group
The algorithm should maximise the number of people each person meets over several iterations"""

# Parameters: [@TODO - make parameters more flexible]
# Students = 80
# Group size = 4

# @TODO Extend for 80 % 4 != 0

# Import packages
from random import choice, seed
from math import ceil
from timeit import timeit
from collections import Counter
import pandas as pd

# Set seed for reproducibility
set_seed = seed(42)

########################################################################################################################
# Building-block functions
########################################################################################################################


def import_list(filename):
    """Function that imports a file and reads a list"""
    with open(filename, 'r') as fp:
        return fp.read().splitlines()


def initialise_group_memory(people_list):
    """ A function that initialises the group memory dict and adds all people from a list as keys"""
    people_dict = {student: [] for student in people_list}  # Initialise group memory
    return people_dict


def initialise_group_dict(n):
    """ Initialises a group dictionary for n groups"""
    group_dict = {i: [] for i in range(1, n + 1)}
    return group_dict


def assign_group(group_dict, group_n, student, student_list):
    """ A function that adds a student to the group and removes them from the main list"""
    group_dict[group_n].append(student)
    student_list.remove(student)
    return group_dict, student_list


def remember_group(group_dict, group, memory):
    """ A function that adds all members of a group to memory, along with the students they have worked with"""
    for student_i in group_dict[group]:
        for student_j in group_dict[group]:
            if student_i != student_j:
                memory[student_i].append(student_j)
    return memory

########################################################################################################################
# Group builder function
########################################################################################################################


def form_group(group_dict, group_n, s_list, memory):
    # Create a loop that runs until the group size = 4
    for s in s_list:
        if len(group_dict[group_n]) == 4:
            break

        # Check whether group is empty, if so, add to group
        if len(group_dict[group_n]) == 0:
            group_dict, s_list = assign_group(group_dict, group_n, s, s_list)
        # Check whether student has  worked with an existing group member before, if so, skip step
        elif len([student for student in group_dict[group_n] if
                  student in memory[s]]) > 0:
            pass
        # If they have not worked with the chosen student, assign to a group
        else:
            group_dict, s_list = assign_group(group_dict, group_n, s, s_list)
    return group_dict, s_list

########################################################################################################################
# Populate n groups
########################################################################################################################


def populate_groups(s_list, memory):
    # Calculate number of groups required
    copy_s_list = list(s_list)
    n_groups = ceil(len(copy_s_list) / 4)
    # Initialise group dictionary
    dictionary_of_groups = initialise_group_dict(n_groups)

    # For each group
    for n in range(1, n_groups + 1):
        # Populate group
        dictionary_of_groups, updated_student_list = form_group(dictionary_of_groups, n, copy_s_list, memory)
        # Remember group
        memory = remember_group(dictionary_of_groups, n, memory)
    return dictionary_of_groups, memory


########################################################################################################################
# MAIN - Populate groups over a number of iterations
########################################################################################################################


def main(filename, iterations):
    """ A function that creates groups from a student list to maximise the number of students each other
    student meets over a specific number of iterations"""

    # Import student list
    s_list = import_list(filename)

    # Initialise memory
    s_memory = initialise_group_memory(s_list)

    # Initialise list of group dictionaries for each iteration
    list_of_group_dicts = []

    # Repeat group population for the required number of iterations
    for i in range(1, iterations + 1):
        # Populate groups
        dictionary_of_groups, s_memory = populate_groups(s_list, s_memory)
        # Add dictionary of groups to list of groups dictionary
        list_of_group_dicts.append(dictionary_of_groups)
    return list_of_group_dicts, s_memory


########################################################################################################################
# Call the function
########################################################################################################################


list_of_groups, s_memory = main('hogwarts_students.csv', 3)
print(list_of_groups[0])
print(list_of_groups[1])
print(list_of_groups[2])
print(s_memory['Hermione Granger'])

#list_of_groups_df = pd.DataFrame(data=list_of_groups[0])
#print(list_of_groups_df)



########################################################################################################################
# Time the functions
########################################################################################################################


#one_it = lambda: main('hogwarts_students.csv', 1)
#two_it = lambda: main('hogwarts_students.csv', 2)
#three_it = lambda: main('hogwarts_students.csv', 3)

#print("One iteration took:")
#print(timeit(one_it, number=1))

#print("Two iterations took:")
#print(timeit(two_it, number=1))

#print("Three iterations took:")
#print(timeit(three_it, number=1))

########################################################################################################################
# Test the functions
########################################################################################################################

# Check that each student is assigned only one group per iteration

def check_gp_numbers(filename, iter):
    # Run the function and return the results
    list_of_groups, s_memory = main(filename, iter)
    number_of_groups = len(list_of_groups[0].keys())

    # For each iteration
    for i in range(iter):
        # Extract the values from each group
        group_lists = [value for value in list_of_groups[i].values()]
        # Add the values into a single list
        student_names = list(group_lists[0])
        for i in range(1, number_of_groups):
            student_names = student_names + group_lists[i]
        # Create a counter of each time a name occurs
        group_count = Counter(student_names)
        # Return any names where count > 1
        errors = [value for value in group_count.values() if value > 1]
    return group_count, errors


#print(check_gp_numbers('hogwarts_students.csv', 40)[0])
#print(check_gp_numbers('hogwarts_students.csv', 40)[1])

# Check that no students are working with students they have previously worked with

def cross_check_memory(student, filename, iter):
    # Run the function and return the results
    list_of_groups, s_memory = main(filename, iter)
    print(list_of_groups)
    # Create a groups list
    groups = []
    # Create a workmate list
    workmates = []
    # For each iteration
    for i in range(1, iter):
        for j in range(len(list_of_groups[i])):
            for key, value in list_of_groups[i]:
                return key, value
        # Return the group the student was in
        # Retun the students in that group
        # Add to student list


#print(cross_check_memory('Ron Weasley', 'hogwarts_students.csv', 2))