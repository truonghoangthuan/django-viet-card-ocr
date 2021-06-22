from .studentCard_class import *
from .idCard_class import *
from .drivingLicense_class import *

def classify(results):
    for item in results:
        if 'CĂN CƯỚC CÔNG DÂN' in item or 'CĂN CƯỚC' in item:
            return 1
        if 'GIẤY PHÉP LÁI XE' in item or 'GIẤY' in item or 'GIÂY PHÉP LÁI XE' in item or 'DRIVER' in item:
            return 2
        # if 'TRƯỜNG ĐẠI HỌC' in item or 'TRƯỜNG ĐAI HOC' in item or 'TRƯỜNG ĐAI' in item or 'UNIVERSITY' in item:
        #     return 3
        if 'SINH VIÊN' in item or 'STUDENT' in item or 'SINH' in item:
            return 3


def output_proc_idCard(results):
    id = ''
    name = ''
    birth = ''
    nationality = ''
    sex = ''
    hometown = ''
    address = ''

    for i in range (len(results)):
        if results[i].isdigit():
            id = results[i]
            if results[i+1] == 'Họ và tên:' or results[i+1] == 'HỌ VÀ TÊN' or results[i+1] == 'Ho và tên' or results[i+1] == 'Họ và tên':
                name = results[i+2]
            else:
                if 'Họ và tên:' in results[i+1] or 'HỌ VÀ TÊN' in results[i+1] or 'Ho và tên' in results[i+1] or 'Họ và tên' in results[i+1]:
                    name = results[i+1][11:]
                else:
                    name = results[i+1]
        if 'Ngày, tháng, năm sinh' in results[i]:
            birth = results[i][22:]
        if 'Quốc tịch' in results[i] or 'Quốc tích' in results[i]:
            nationality = results[i][11:]
        if 'Giới tính' in results[i] or 'GIỚI TÍNH' in results[i] or 'Giới tinh' in results[i] or 'Giới' in results[i]:
            sex = results[i][10:]
        if 'Quê quán' in results[i] or 'Quê quân' in results[i]:
            hometown = results[i][10:]
            if 'Nơi thường trú:' not in results[i+1]:
                hometown += " "+ results[i+1]
        if 'Nơi thường trù' in results[i] or 'Nơi thường trú' in results[i] or 'Nơi thường' in results[i]:
            address = results[i][16:]
            if 'Có giá trị đến' not in results[i+1]:
                address += " "+results[i+1]
    
    idCard = IdCard(id,name,birth,nationality,sex,hometown,address)
    return idCard

def output_proc_drivingLicense(results):
    idOfDL = ''
    nameOfDL = ' '
    birthOfDL = ''
    nationalityOfDL = ''
    addressOfDL = ''
    classOfDL = ''

    for i in range (len(results)):
        if results[i].isdigit():
            idOfDL = results[i]
        elif 'Số/No' in results[i] or  'Sô/No' in results[i] :
            idOfDL = results[i][7:]
        elif 'Số' in results[i] or 'No' in results[i]:
            idOfDL = results[i][4:]
        if idOfDL in results[i]:
            if results[i+1] == 'Họ tên/Full name:' or results[i+1] == 'Ho tên/Full name' or results[i+1] == 'Họ tên/Full name':
                nameOfDL = results[i+2]
            elif 'Họ tên' in results[i+1]:
                nameOfDL = results[i+2]
            else:
                nameOfDL = results[i+1]
        if 'Ngày sinh' in results[i] or 'Birth' in results[i]:
            if '/' in results[i-1]:
                birthOfDL = results[i-1]
            else:
                birthOfDL = results[i+1]
            if 'Full name' in results[i-1]:
                birthOfDL = results[i+1]
        if 'Quốc tịch' in results[i]:
            if 'NAM' in results[i-1] or 'Address' in results[i+1]:
                nationalityOfDL = results[i-1]
            else:
                nationalityOfDL = results[i+1]
        if 'Nơi cư trù' in results[i] or 'Nơi cư trú' in results[i] or 'Address' in results[i]:
            # addressOfDL = results[i+1]
            if 'Quốc tịch/Nationality:' in results[i-1] or 'NAM' in results[i-1] or 'Nationality' in results[i-1]:
                addressOfDL = results[i+1]
            else:
                addressOfDL = results[i-1] + ', ' + results[i+1]
            if 'năm' in results[i+1]:
                addressOfDL = results[i-1]
            if 'korea' in results[i-1]:
                addressOfDL = results[i+1]
            if 'year' in results[i+2] or 'date' in results[i+2] or 'ngôy' in results[i+2] or 'velome' in results[i+2]:
                continue
            else:
                addressOfDL += ', ' + results[i+2]
        if 'Hạng' in results[i]:
            classOfDL = results[i][11:]
    
    drivingLicense = DrivingLicense(idOfDL,nameOfDL,birthOfDL,nationalityOfDL,addressOfDL, classOfDL)
    return drivingLicense

def output_proc_studentCard(results):
    id = ''
    name = ''
    major = ''
    faculty = ''
    course = ''

    for i in range (len(results)):
        if 'SINH VIÊN' in results[i] or 'sinh viên' in results[i] or 'STUDENT' in results[i]:
            name = results[i+1]
            id = results[i+2]
            faculty = results[i-1]
        if 'Ngành' in results[i] or 'Nganh' in results[i] or 'Major' in results[i]:
            major = results[i][6:]
        if 'Khóa học' in results[i] or 'Khoa học' in results[i]:
            course = results[i][9:]
        if 'Course' in results[i]:
            course = results[i][7:]

    studentCard = StudentCard(name, id, major, faculty, course)
    return studentCard

