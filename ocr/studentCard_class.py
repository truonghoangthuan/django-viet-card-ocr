class StudentCard:
    def __init__(self, name, id, major, faculty, course):
        self.name = name
        self.id = id
        self.major = major
        self.faculty = faculty
        self.course = course


    def print_StudentCard(self):
        dic = {
            'ID': self.id,
            'Name': self.name,
            'Major': self.major,
            'Falculty': self.faculty,
            'Coures': self.course
        }

        return dic

        