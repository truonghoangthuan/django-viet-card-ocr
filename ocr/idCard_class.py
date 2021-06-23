class IdCard:
    def __init__(self, id, name, birth, nationality, sex, hometown, address):
        self.id = id
        self.name = name
        self.birth = birth
        self.nationality = nationality
        self.sex = sex
        self.hometown = hometown
        self.address = address

    def print_idCard(self):
        # result = 'CMND: ' + self.id + \
        #          '\nName: ' + self.name + \
        #          '\nDOB ' + self.birth + \
        #          '\nNationality: ' + self.nationality + \
        #          '\nSex: ' + self.sex + \
        #          '\nHometown: ' + self.hometown + \
        #          '\nAddress: ' + self.address
        dic = {
            "CMND" : self.id,
            "Name" : self.name,
            "DOB" : self.birth,
            "Nationality" : self.nationality,
            "Sex" : self.sex,
            "Hometown" : self.hometown,
            "Address" : self.address
        }
        result = ''
        for key, value in dic.items():
            result += str(key) + ' : ' + str(value) + "\n"
        return result