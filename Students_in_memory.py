""" Subscript to practice checking whether students have worked together before"""

group_dict = {'Group_1': ['Fred', 'George', 'Harry']}

chosen_student = 'Hermione'

group_memory = {'Hermione': []}

print(group_dict['Group_1'])

print([student for student in group_dict['Group_1']])
print([student for student in group_dict['Group_1'] if student in group_memory[chosen_student]])

for student in group_dict['Group_1']:
    if student in group_memory[chosen_student]:
        print(student)