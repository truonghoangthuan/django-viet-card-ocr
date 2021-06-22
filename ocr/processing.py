import cv2
import numpy as np
from math import *
from .ctpn_predict import get_det_boxes
from .ocr import img_to_text


def show_image(image):
    cv2.imshow('image', image)
    cv2.waitKey(0)
#hàm hiển thị


def sort_box(box):
    box = sorted(box, key=lambda x: sum([x[1], x[3], x[5], x[7]]))
    # box = sorted(box, cv2.con)

    return box
#hàm sắp xếp các trường


def rotate_image(img, degree, pt1, pt2, pt3, pt4):
     
    height, width = img.shape[:2]
    heightNew = int(width * fabs(sin(radians(degree))) + height * fabs(cos(radians(degree))))
    widthNew = int(height * fabs(sin(radians(degree))) + width * fabs(cos(radians(degree))))

    matRotation = cv2.getRotationMatrix2D((width // 2, height // 2), degree, 1)
    matRotation[0, 2] += (widthNew - width) // 2
    matRotation[1, 2] += (heightNew - height) // 2

    imgRotation = cv2.warpAffine(img, matRotation, (widthNew, heightNew), borderValue=(255, 255, 255))

    pt1 = list(pt1)
    pt3 = list(pt3)

    [[pt1[0]], [pt1[1]]] = np.dot(matRotation, np.array([[pt1[0]], [pt1[1]], [1]]))
    [[pt3[0]], [pt3[1]]] = np.dot(matRotation, np.array([[pt3[0]], [pt3[1]], [1]]))

    ydim, xdim = imgRotation.shape[:2]

    imgOut = imgRotation[max(1, int(pt1[1])): min(ydim - 1, int(pt3[1])),
             max(1, int(pt1[0])): min(xdim - 1, int(pt3[0]))]
    
    return imgOut
    
#Hàm xoay ảnh


def char_rec(img, text_recs, adjust=False):
    
    results = []
    list_img = []
    xDim, yDim = img.shape[1], img.shape[0]

    for index, rec in enumerate(text_recs):
        xlength = int((rec[6] - rec[0]) * 0.1)
        ylength = int((rec[7] - rec[1]) * 0.2)
        if adjust:
            pt1 = (max(1, rec[0] - xlength), max(1, rec[1] - ylength))
            pt2 = (rec[2], rec[3])
            pt3 = (min(rec[6] + xlength, xDim - 2), min(yDim - 2, rec[7] + ylength))
            pt4 = (rec[4], rec[5])
        else:
            pt1 = (max(1, rec[0]), max(1, rec[1]))
            pt2 = (rec[2], rec[3])
            pt3 = (min(rec[6], xDim - 2), min(yDim - 2, rec[7]))
            pt4 = (rec[4], rec[5])

        degree = degrees(atan2(pt2[1] - pt1[1], pt2[0] - pt1[0]))  
        part_img = rotate_image(img, degree, pt1, pt2, pt3, pt4) #xoay ảnh vào cắc từng trường

        if part_img.shape[0] < 1 or part_img.shape[1] < 1 or part_img.shape[0] > part_img.shape[1]:  
            continue
        
        list_img.append(part_img)
        
        

    results = img_to_text(list_img)
    

    return results
#Hàm nhận dạng kí tự


def proc_img(image):
    # detect
    text_recs, img_framed, image = get_det_boxes(image) #gọi hàm get_det_boxes trả về ảnh đã vẽ (img_framed), tọa độ cắt ảnh (test_recs)
    text_recs = sort_box(text_recs) #sắp xếp các trường
    result = char_rec(image, text_recs) #nhận diện , đầu vào là file tọa độ và hình ảnh ban đầu
    return result, img_framed
