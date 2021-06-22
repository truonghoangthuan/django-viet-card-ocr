import cv2
import numpy as np
from PIL import Image

from .classify import *
from .processing import proc_img


def single_pic_proc(image_file):
    image = np.array(Image.open(image_file).convert('RGB'))  # chuyển ảnh xám
    result, image_framed = proc_img(image)  # nhận dạng, gọi hàm proc_img của module processing
    return result, image_framed  # trả về


# Hàm xử lí ảnh trả về ảnh đã vẽ khung và kết quả nhận dạng


def show_img(image):
    cv2.imshow('image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Hàm hiển thị ảnh


def print_list_text(list_img):
    for text in list_img:
        print('TEXT OUTPUT:' + text)


# Hàm in danh sách kết quả


def output_proc(results):  # xử lí kết quả đầu ra
    id = ' '
    name = ' '
    birth = ' '
    nationality = ' '
    sex = ' '
    hometown = ' '
    address = ' '
    classOfDL = ' '
    major = ' '
    faculty = ' '
    course = ' '
    if classify(results) == 1:
        card = IdCard(id, name, birth, nationality, sex, hometown, address)
        card = output_proc_idCard(results)
        card.print_idCard()
    if classify(results) == 2:
        card = DrivingLicense(id, name, birth, nationality, address, classOfDL)
        card = output_proc_drivingLicense(results)  # phân loại
        card.print_DrivingLicense()
    if classify(results) == 3:
        card = StudentCard(name, id, major, faculty, course)
        card = output_proc_studentCard(results)
        card.print_StudentCard()


# if __name__ == '__main__':
#     import sys
#     if len(sys.argv)>=2:
#         filename = sys.argv[1]
#         if filename.endswith('jpg') or filename.endswith('png'): #nhận đầu vào là đuôi jpg hoặc png
#             results, image_framed = single_pic_proc(filename) #Hàm trả về là kết quả dạng array và img đã đóng khung
#             print(results) #hiển thị kết quả
#             output_proc(results)
#             show_img(image_framed) #hiển thị ảnh
def extract(img):
    results, image_framed = single_pic_proc(img)  # Hàm trả về là kết quả dạng array và img đã đóng khung
    output_proc(results)


# extract('images/cmnd6.jpg')
