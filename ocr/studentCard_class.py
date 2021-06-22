class StudentCard:
    def __init__(self, name, id, major, faculty, course):
        self.name = name
        self.id = id
        self.major = major
        self.faculty = faculty
        self.course = course


    def print_StudentCard(self):
        print('Họ tên: ' + self.name)
        print('MSSV: ' + self.id)
        print('Ngành: ' + self.major)
        print('Khoa: ' + self.faculty)
        print('Khóa học: ' + self.course)

        