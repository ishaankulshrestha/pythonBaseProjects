class Students:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def comparator(a, b):
        if a.marks != b.marks:
            if a.marks < b.marks:
                return 1
            elif a.marks > b.marks:
                return -1
            else:
                return 0
        else:
            if a.name > b.name:
                return 1
            elif a.name < b.name:
                return -1
            else:
                return 0


print("Enter number of students ")
n = input()

data = []
for i in range(n):
    print("Enter Name and marks of student %d" % (i + 1))
    name, marks = input().split()
    marks = int(marks)
    player = Students(name, marks)
    data.append(player)

data = sorted(data, cmp=Students.comparator)
print
"\nStudents Name and marks in sorted form "
print
"Name \t Marks"
print
"----------------"
for i in data:
    print
    i.name + " \t " + str(i.marks)