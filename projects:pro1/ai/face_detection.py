import requests
import base64
import cv2 as cv
from PIL import Image, ImageDraw, ImageFont
import numpy as np
def face_detection(img):
    '''
    人体检测和属性识别
    '''

    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/body_attr"

    # 二进制方式打开图片文件

    _, encoded_image = cv.imencode('.jpg', img)
    base64_image = base64.b64encode(encoded_image)

    params = {"image": base64_image}
    access_token = '24.5062ad79993872bc75325e6d3228e6cf.2592000.1722778131.282335-91079926'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    data = response.json()


    # 将图像转换为Pillow格式
    pil_image = Image.fromarray(cv.cvtColor(img, cv.COLOR_BGR2RGB))

    # 创建一个Draw对象
    draw = ImageDraw.Draw(pil_image)

    # 加载字体（请将路径替换为您系统中的中文字体路径）
    font_path = "/System/Library/Fonts/STHeiti Light.ttc"
    font = ImageFont.truetype(font_path, 36)

    # 遍历每个人的信息
    if 'person_info' in data:
        for person in data["person_info"]:
            attributes = person["attributes"]
            location = person["location"]

            # 提取关键信息
            gender = attributes["gender"]["name"]
            age = attributes["age"]["name"]
            upper_wear = attributes["upper_wear"]["name"]
            lower_wear = attributes["lower_wear"]["name"]

            # 获取位置参数
            x, y, w, h = location["left"], location["top"], location["width"], location["height"]

            # 绘制矩形框
            draw.rectangle([x, y, x + w, y + h], outline="green", width=3)

            # 绘制文本
            text = f"{gender}, {age}, {upper_wear}, {lower_wear}"
            draw.text((x, y - 40), text, font=font, fill="green")

        # 将图像转换回OpenCV格式
        cv_image = cv.cvtColor(np.array(pil_image), cv.COLOR_RGB2BGR)

        # 显示图像

    return  cv_image