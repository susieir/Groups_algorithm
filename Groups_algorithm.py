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
    people_dict = {}  # Initialise group memory
    for item in people_list:
        people_dict[item] = []
    return people_dict

def assign_group(group, student, student_list):
    """ A function that adds a student to the group and removes them from the main list"""
    group.append(student)
    student_list.remove(student)
    return group, student_list


group_memory = initialise_group_memory(harrys_friends)  # Initialise group memory
group_memory['Fred'] = 'George'
group_memory['George'] = 'Fred'
#print(group_memory['Ginny'])

# For a given number of iterations: [@TODO - Add functionality]
# Until the list of students is empty for the number of required groups (8 0 /4=20): [@TODO - Add functionality]


# Make a copy of the student list
copy_student_list = list(harrys_friends)

def form_group(s_list, memory): #[@TODO - Add variables for group numbers and group size] [@TODO - Create function]
    # Add a group with an empty list to the dictionary, to which students will be added
    group_1 = []

    # Create a loop that runs until the group size = 4
    while len(group_1) <= 4:
        if len(group_1) == 4:
            break
    # Randomly select a student from the copy list
        chosen_student = choice(s_list)
        print("Chosen student is {b}".format(b=chosen_student))

        # Run checks
        # Check 1 - Is the group empty?
        if len(group_1) == 0:
            # Add to the group
            group, s_list = assign_group(group_1, chosen_student, s_list)
            print("First group member is {}".format(chosen_student))
            print(len(group_1))
            print(s_list)
        # Check 2 - Have they worked with an existing group member before
        elif len([student for student in group_1 if student in memory[chosen_student]])>0: #[@TODO - fix elif]
            print("Students have worked together, {} not added to group".format(chosen_student))
            pass
                # The loop should begin again without adding the chosen student to the list
            # If they have not worked with the chosen student
        else:
            # Add them to the group and remove from the student list
            group, s_list = assign_group(group_1, chosen_student, s_list)
            print("{} added to group".format(chosen_student))
            print(s_list)
            print(len(group_1))
        # Add all students in group to memory
    print(group_1)
    for student_i in group_1:
        for student_j in group_1:
            if student_i != student_j:
                memory[student_i] = student_j
    return group_1, memory, s_list

group_1, mem, revised_s_list = form_group(harrys_friends, group_memory)

print("Group 1 is \n{}".format(group_1))
print("Memory is \n{}".format(mem))
print("Latest student list is \n{}".format(revised_s_list))

#    print("Copy student list: \copy_student_list)
#    print(group_memory)




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
