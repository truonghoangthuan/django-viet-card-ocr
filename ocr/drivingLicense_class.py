class DrivingLicense:
    def __init__(self,id, name, birth, nationality, address, classOfDL):
        self.id = id
        self.name = name
        self.birth = birth
        self.nationality = nationality
        self.address = address
        self.classOfDL = classOfDL

    def print_DrivingLicense(self):
        dic = {
            'ID': self.id,
            'Name': self.name,
            'DOB': self.birth,
            'Nationality': self.nationality,
            'Address': self.address,
            'Class': self.classOfDL
        }

        return dic