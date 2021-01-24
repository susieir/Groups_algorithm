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
# Group builder function
########################################################################################################################


def form_group(group_dict, group_n, s_list, memory):
    # Create a loop that runs until the group size = 4
    while len(group_dict[group_n]) <= 4:
        if len(group_dict[group_n]) == 4:
            break
        # Randomly select a student from the copy list
        chosen_student = choice(s_list)
        #        print("Chosen student is {}".format(chosen_student))

        # Check whether group is empty
        if len(group_dict[group_n]) == 0:
            # If so, add student to group
            group_dict, s_list = assign_group(group_dict, group_n, chosen_student, s_list)
        #                print(group_dict)
        #                print(type(group_dict))
        # Check whether student has  worked with an existing group member before
        elif len([student for student in group_dict[group_n] if
                  student in memory[chosen_student]]) > 0:
            pass
        # If they have not worked with the chosen student, assign to a group
        else:
            group_dict, s_list = assign_group(group_dict, group_n, chosen_student, s_list)
    #                print(group_dict)
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
    return list_of_group_dicts


########################################################################################################################
# Call the function
########################################################################################################################


list_of_groups = main('hogwarts_students.csv', 2)
print(list_of_groups[0])
print(list_of_groups[1])
#print(list_of_groups[2])
#print(group_memory)

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
