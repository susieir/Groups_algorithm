# Groups_algorithm

An algorithm that maximises that number of people each student in a class meets over the course of a number of group exercises.
Groups are randomly allocated, avoiding placing two students who have worked before together.

**Work in progress**: Algorithm functions and takes a csv input - manually checked for up to three iterations

Next steps:
- Build testing function to check accuracy on more than three iterations
- Build csv/xls export of groups for each iteration
- Review limitations/possible extensions and put in place (or document)

Limitations:
- Only works where the class size (n) is n % 4 == 0
- Class size is fixed (turn into a param)
