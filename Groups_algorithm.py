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
student_list = ['Fred', 'George', 'Harry', 'Hermione', 'Ron', 'Ginny']

# Initialise a N dictionaries for each iteration (group_dict_N) [@TODO - create function]
group_dict_1 = {}


def initialise_group_memory(people_list):
    """ A function that initialises the group memory dict and adds all people from a list as keys"""
    people_dict = {}  # Initialise group memory
    for item in people_list:
        people_dict[item] = []
    return people_dict


group_memory = initialise_group_memory(student_list)  # Initialise group memory
group_memory['Fred'] = 'George'
group_memory['George'] = 'Fred'
#print(group_memory['Ginny'])

# For a given number of iterations: [@TODO - Add functionality]
# Until the list of students is empty for the number of required groups (8 0 /4=20): [@TODO - Add functionality]


# Make a copy of the student list
copy_student_list = list(student_list)

#def form_group(s_list, memory): #[@TODO - Add variables for group numbers and group size] [@TODO - Create function]
# Add a group with an empty list to the dictionary, to which students will be added
group_dict_1['group_1'] = []

# Create a loop that runs four times to add students to the group dictionary for that iteration:
while len(group_dict_1['group_1']) <= 4:
# Randomly select a student from the copy list
    chosen_student = choice(copy_student_list)
    print("Chosen student is {b}".format(b=chosen_student))

# Run checks
# Check 1 - Is the group empty?
    if len(group_dict_1['group_1']) == 0:
        # Add to the group
        group_dict_1['group_1'].append(chosen_student)
        copy_student_list.remove(chosen_student)
        print("First group member is {}".format(chosen_student))
        print(copy_student_list)
    # Check 2 - Have they worked with an existing group member before
    elif len([student for student in group_dict_1['group_1'] if student in group_memory[chosen_student]])>0: #[@TODO - fix elif]
        print("Students have worked together, {} not added to group".format(chosen_student))
        pass
                # The loop should begin again without adding the chosen student to the list
            # If they have not worked with the chosen student
    else:
        # Add them to the group and remove from the student list
        group_dict_1['group_1'].append(chosen_student)
        print("{} added to group".format(chosen_student))
        copy_student_list.remove(chosen_student)
        print(copy_student_list)
    print(group_dict_1)
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
