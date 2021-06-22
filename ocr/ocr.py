import numpy as np
from vietocr.tool.predictor import Predictor
from vietocr.tool.config import Cfg
from PIL import Image
import cv2


def img_to_text(list_img):
    results = []
    for i in range(len(list_img)):
        if i == 0 or i == len(list_img) - 1:
            continue
        # sử dụng config mặc định của mô hình
        config = Cfg.load_config_from_name('vgg_transformer')
        # đường dẫn đến trọng số đã huấn luyện hoặc comment để sử dụng #pretrained model mặc định
        config['weights'] = 'ocr/transformerocr.pth'
        config['device'] = 'cpu' # device chạy 'cuda:0', 'cuda:1', 'cpu'

        detector = Predictor(config)
        img = Image.fromarray(list_img[i].astype(np.uint8))
        # img = Image.fromarray((img * 255).astype(np.uint8))
        # img.show()

        # dự đoán 
        # muốn trả về xác suất của câu dự đoán thì đổi return_prob=True
        text = detector.predict(img)

        if len(text) > 0:
            results.append(text)
    return results


