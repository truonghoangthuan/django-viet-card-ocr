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
        # print('Số CMND: ' + self.id)
        # print('Họ tên: ' + self.name)
        # print('Ngày sinh: ' + self.birth)
        # print('Quốc tịch: ' + self.nationality)
        # print('Giới tính: ' + self.sex)
        # print('Quê quán: ' + self.hometown)
        # print('Địa chỉ thường trú: ' + self.address)
        result = 'CMND: ' + self.id + \
                 '\nName: ' + self.name + \
                 '\nDOB ' + self.birth + \
                 '\nNationality: ' + self.nationality + \
                 '\nSex: ' + self.sex + \
                 '\nHometown: ' + self.hometown + \
                 '\nAddress: ' + self.address
        print(result)
