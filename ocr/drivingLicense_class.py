class DrivingLicense:
    def __init__(self, id, name, birth, nationality, address, classOfDL, expires):
        self.id = id
        self.name = name
        self.birth = birth
        self.nationality = nationality
        self.address = address
        self.classOfDL = classOfDL
        self.expires = expires

    def print_DrivingLicense(self):
        dic = {
            'ID': self.id,
            'Name': self.name,
            'DOB': self.birth,
            'Nationality': self.nationality,
            'Address': self.address,
            'Class': self.classOfDL,
            'Expires': self.expires
        }

        return dic