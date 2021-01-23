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


print(group_dict['Group_1'][1])

group_1 = ['Ginny', 'Fred', 'Hermione', 'Ron']

dict_a = {'Ginny' : [], 'Hermione': [], 'Ron' : [], 'Fred' : []}
dict_b = {student: [] for student in group_1}
print(dict_b)

for student_i in group_1:
    for student_j in group_1:
        if student_i != student_j:
            dict_b[student_i].append(student_j)
            print(dict_b)

