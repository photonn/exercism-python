class School:
    def __init__(self):
        self.students = {}

    def add_student(self, name, grade):
        self.students[name]=grade

    def roster(self):
        return [x[0] for x in sorted(self.students.items(), key = lambda kv:(kv[1], kv[0]))]

    def grade(self, grade_number):
        return sorted([student for student in self.students if self.students[student] == grade_number])