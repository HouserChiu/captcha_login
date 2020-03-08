import pytesseract
from urllib import request
from PIL import Image
import time

def main():
    pytesseract.pytesseract.tesseract_cmd = r'D:\tesseract\tesseract.exe'
    url = 'https://id.ifeng.com/index.php/public/authcode?1583655369885'
    while True:
        #打开URL保存为captcha.png
        request.urlretrieve(url, 'captcha.png')
        image = Image.open('captcha.png')
        text = pytesseract.image_to_string(image)
        print(text)
        time.sleep(2)


if __name__ == '__main__':
    main()