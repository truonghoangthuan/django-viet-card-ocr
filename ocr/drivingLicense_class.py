class DrivingLicense:
    def __init__(self,id, name, birth, nationality, address, classOfDL):
        self.id = id
        self.name = name
        self.birth = birth
        self.nationality = nationality
        self.address = address
        self.classOfDL = classOfDL

    def print_DrivingLicense(self):
        print('Số: ' + self.id)
        print('Họ tên: '+ self.name)
        print('Ngày sinh: '+ self.birth)
        print('Quốc tịch: '+ self.nationality)
        print('Nơi cư trú: '+ self.address)
        print('Hạng: ' + self.classOfDL)