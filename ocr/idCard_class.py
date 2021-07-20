class IdCard:
    def __init__(self, id, name, birth, nationality, sex, hometown, address, expires):
        self.id = id
        self.name = name
        self.birth = birth
        self.nationality = nationality
        self.sex = sex
        self.hometown = hometown
        self.address = address
        self.expires = expires

    def print_idCard(self):
        dic = {
            "ID" : self.id,
            "Name" : self.name,
            "DOB" : self.birth,
            "Nationality" : self.nationality,
            "Sex" : self.sex,
            "Hometown" : self.hometown,
            "Address" : self.address,
            "Expires" : self.expires,
        }
        
        return dic