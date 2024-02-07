class Studentiki:
    id = 0
    fio = ''
    id_project = 0
    clas = ''
    score = 0

students = []
f = open('students.csv')
j = 0
for i in f:
    s = i.split(',')
    if int(s[3][:-1]) == 10:
        students.append(Studentiki())
        students[j].fio = s[1]
        students[j].score = int(s[4])
        j += 1

for i in range(len(students)-1):
    for j in range(len(students)-1-i):
        if students[j].score < students[j+1].score:
            students[j], students[j+1] = students[j+1], students[j]
print(students[0].fio)
print(students[1].fio)
print(students[2].fio)
