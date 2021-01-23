# Groups_algorithm

An algorithm that maximises that number of people each student in a class meets over the course of a number of group exercises.
Groups are randomly allocated, avoiding placing two students who have worked before together.

*** Work in progress **: Currently allocates n groups based on a list of n*4 students, whilst creating a group memory

Next steps:
- Fix group memory - currently some students have too many other students in memory
- Extend for multiple iterations
- Update for a csv class list input
- Review limitations and fix (or document)

Limitations:
- Only works where the class size (n) is n % 4 == 0
- Class size is fixed (turn into a param)
