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

student_list = ['Fred', 'George', 'Harry', 'Hermione']

# Create a list of students
# Initialise a lookup that will keep a record of who each student has worked with (group_memory)
group_memory = {'Hermione': 'Fred'}
# Initialise a N dictionaries for each iteration (group_dict_N) [@TODO - create function]
group_dict_1 = {}
group_dict_2 = {}
group_dict_3 = {}

# For a given number of iterations:
#   Until the list of students is empty for the number of required groups (8 0 /4=20):
#       Add a group with an empty list to the dictionary, to which students will be added
group_dict_1['group_1'] = []
#       Make a copy of the student list
copy_student_list = student_list
# Create a loop that runs four times to add students to the group dictionary for that iteration:
for i in range(4):
# Randomly select a student from the copy list
    chosen_student = choice(copy_student_list)
    print("Chosen student {a} is {b}".format(a=i, b=chosen_student))

# If the group is empty - add the student to the group dictionary and remove from the copy list
    if group_dict_1['group_1'] == []:
        group_dict_1['group_1'].append(chosen_student)
        copy_student_list.remove(chosen_student)
        print(copy_student_list)
        print(group_dict_1)
    else:
        group_dict_1['group_1'].append(chosen_student)
        copy_student_list.remove(chosen_student)
        print(copy_student_list)
        print(group_dict_1)

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