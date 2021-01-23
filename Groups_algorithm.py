### Groups algorithm
### Version 0.1
"""Challenge:
Create an algorithm which randomly assigns a list of students to a group
The algorithm should maximise the number of people each person meets over several iterations"""

#Parameters:
#Students = 80
#Group size = 4

# Import packages
from random import choice, seed

# Set seed for reproducibility
set_seed = seed(42)

# Student list input [@TODO - add functionality to read from csv]
harrys_friends = ['Fred', 'George', 'Harry', 'Hermione', 'Ron', 'Ginny']

# Initialise a N dictionaries for each iteration (group_dict_N) [@TODO - create function]
#group_dict_1 = {}


def initialise_group_memory(people_list):
    """ A function that initialises the group memory dict and adds all people from a list as keys"""
    people_dict = {student: [] for student in people_list}  # Initialise group memory
    return people_dict

def assign_group(group, student, student_list):
    """ A function that adds a student to the group and removes them from the main list"""
    group.append(student)
    student_list.remove(student)
    return group, student_list

def remember_group(group, memory):
    """ A function that adds all members of a group to memory, along with the students they have worked with"""
    for student_i in group:
        for student_j in group:
            if student_i != student_j:
                memory[student_i].append(student_j)
    return memory




#group_memory = initialise_group_memory(harrys_friends)  # Initialise group memory
#group_memory['Fred'] = 'George'
#group_memory['George'] = 'Fred'
#print(group_memory['Ginny'])

# For a given number of iterations: [@TODO - Add functionality]
# Until the list of students is empty for the number of required groups (8 0 /4=20): [@TODO - Add functionality]



def form_group(s_list, memory): #[@TODO - Add variables for group numbers and group size] [@TODO - Create function]
    # Add a group with an empty list to the dictionary, to which students will be added
    group_1 = []

    # Create a loop that runs until the group size = 4
    while len(group_1) <= 4:
        if len(group_1) == 4:
            break
    # Randomly select a student from the copy list
        chosen_student = choice(s_list)

        # Run checks
        # Check 1 - Is the group empty?
        if len(group_1) == 0:
            # Add to the group
            group, s_list = assign_group(group_1, chosen_student, s_list)
        # Check 2 - Have they worked with an existing group member before
        elif len([student for student in group_1 if student in memory[chosen_student]])>0: #[@TODO - fix elif]
            pass
            # If they have not worked with the chosen student, assign to a group
        else:
            group, s_list = assign_group(group_1, chosen_student, s_list)
        # Add all students in group to memory
    return group_1, s_list


## 1. Initialise group memory
group_memory = initialise_group_memory(harrys_friends)

## 2. Copy student list
#copy_student_list = list(harrys_friends)

## 3. Form group
group_1, harrys_list_updated = form_group(harrys_friends, group_memory)

## 4. Remember group
group_memory = remember_group(group_1, group_memory)

## 5. Return outcome
print("Group is {}".format(group_1))
print("Group memory is \n{}".format(group_memory))
print("Updated student list is {}".format(harrys_list_updated))


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
