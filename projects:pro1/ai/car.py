import requests
import base64
import cv2 as cv
import numpy as np
from PIL import Image, ImageDraw, ImageFont

def vehicle_detect(img):
    # 车辆检测API
    vehicle_detect_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/vehicle_detect"
    _, encoded_image = cv.imencode('.jpg', img)
    base64_image = base64.b64encode(encoded_image)
    params = {"image": base64_image}
    access_token = '24.9ed0cb58cc020d6e1a149716997aadea.2592000.1722483205.282335-89935330'
    vehicle_detect_url = vehicle_detect_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(vehicle_detect_url, data=params, headers=headers)

    num = 0
    data_car = {}

    if response:
        data_car = response.json()
        print("Vehicle detect response:", data_car)  # 打印车辆检测响应以进行调试

    # 车牌识别API
    license_plate_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/license_plate"
    # 二进制方式打开图片文件
    params = {"image": base64_image}
    access_token = '24.b448f84c2c2f31a12ef330fd84f1828b.2592000.1722952530.282335-91883193'
    license_plate_url = license_plate_url + "?access_token=" + access_token
    response = requests.post(license_plate_url, data=params, headers=headers)

    data_number = {}
    if response:
        data_number = response.json()
        print("License plate response:", data_number)  # 打印车牌识别响应以进行调试

    # 初始化PIL图像
    pil_image = Image.fromarray(cv.cvtColor(img, cv.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(pil_image)
    font = ImageFont.load_default()

    # 绘制车辆检测结果
    if 'vehicle_num' in data_car:
        num = data_car['vehicle_num']['car']
        for item in data_car['vehicle_info']:
            location = item['location']
            x1 = location['left']
            y1 = location['top']
            x2 = x1 + location['width']
            y2 = y1 + location['height']
            draw.rectangle([x1, y1, x2, y2], outline="green", width=2)
            # 定义要绘制的文字
            text = item['type']
            draw.text((x1, y1 - 10), text, font=font, fill="green")

    # 绘制车牌识别结果
    if 'words_result' in data_number:
        result = data_number['words_result']
        if isinstance(result, dict):  # 确保 result 是字典
            number = result.get('number', '')
            location = result.get('vertexes_location', [])
            if number and location:
                print(f"Drawing license plate: {number} at {location}")  # 调试信息
                # 提取四个顶点的坐标
                pts = np.array([[loc['x'], loc['y']] for loc in location], np.int32)
                pts = pts.reshape((-1, 1, 2))
                # 在图像上绘制车牌位置
                draw.polygon([tuple(pt[0]) for pt in pts], outline="red")
                # 在图像上绘制车牌号
                x, y = pts[0][0]
                draw.text((x, y - 10), number, font=font, fill="red")

    # 将图像转换回OpenCV格式
    cv_image = cv.cvtColor(np.array(pil_image), cv.COLOR_RGB2BGR)

    return cv_image, num

