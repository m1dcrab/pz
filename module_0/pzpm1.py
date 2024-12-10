grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)
students.sort()
stud_count = 0
newDict = {}
for x in range(len(students)):
    gradesAverage = sum(grades[stud_count])/len(grades[stud_count])
    newDict.update({students[stud_count]: gradesAverage})
    stud_count = stud_count + 1
print(newDict)