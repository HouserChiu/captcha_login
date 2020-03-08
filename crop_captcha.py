from selenium import webdriver
from PIL import Image
import time

driver = webdriver.Chrome()
driver.get("http://www.4399.com")
driver.find_element_by_xpath('//*[@id="login_tologin"]').click()
#截图格式必须为.png格式
driver.save_screenshot("bdbutton.png")

#新窗口，iframe，Chrome浏览器中下方
ele = driver.find_element_by_id('popup_login_frame')
#获取表单的X坐标，距离左边的距离
f_left = ele.location['x']
#获取距离上方的距离
f_top = ele.location['y']

print(f_left, f_top)
#距离左边的距离（x坐标）+表单宽度，得到图片右上边坐标
f_right = f_left+ele.size['width']
#距离上方的距离（y坐标）+表单高度，得到图片右下角坐标
f_bottom = f_top+ele.size['height']
im = Image.open('bdbutton.png')
#传入坐标进行切割，得到新的窗口截图,以元组形式
im = im.crop((f_left, f_top, f_right, f_bottom))

im.save("b.png")

driver.switch_to.frame('popup_login_frame')
#获取验证码位置
yele = driver.find_element_by_xpath('//*[@id="captcha"]')
y_left = yele.location['x']
#获取距离上方的距离
y_top = yele.location['y']

print(y_left, y_top)
#距离左边的距离（x坐标）+表单宽度，得到图片右上边坐标
y_right = y_left+yele.size['width']
#距离上方的距离（y坐标）+表单高度，得到图片右下角坐标
y_bottom = y_top+yele.size['height']
im = Image.open('b.png')
#传入坐标进行切割，得到新的窗口截图
im = im.crop((y_left, y_top, y_right, y_bottom))

im.save("a.png")

