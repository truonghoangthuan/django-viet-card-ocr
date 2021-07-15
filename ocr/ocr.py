import numpy as np
from vietocr.tool.predictor import Predictor
from vietocr.tool.config import Cfg
from PIL import Image
import time
import matplotlib.pyplot as plt
from PIL import Image


def img_to_text(list_img):
    results = []
    config = Cfg.load_config_from_name('vgg_transformer')
    config['cnn']['pretrained']=True
    config['device'] = 'cpu'
    config['predictor']['beamsearch']=False

    detector = Predictor(config)

    for i in range(len(list_img)):
        if i == 0 or i == len(list_img) - 1:
            continue
        # sử dụng config mặc định của mô hình
        img = Image.fromarray(list_img[i].astype(np.uint8))
        # img = Image.fromarray((img * 255).astype(np.uint8))
        # img.show()

        # dự đoán 
        # muốn trả về xác suất của câu dự đoán thì đổi return_prob=True
        text = detector.predict(img)

        if len(text) > 0:
            results.append(text)
    return results