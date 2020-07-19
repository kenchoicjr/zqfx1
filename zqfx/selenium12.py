import pytesseract
from PIL import Image
from PIL import ImageEnhance
# import tesserocr


def readImage(path):
    img = Image.open(path)  # 根据地址，读取图片
    imgry = img.convert('L')  # 图像加强，二值化
    sharpness = ImageEnhance.Contrast(imgry)  # 对比度增强
    sharp_img = sharpness.enhance(2.0)
    sharp_img.save("new.png")  # 将处理后的图片，保存为new.png
    image = Image.open('new.png')  # 打开处理后的图片
    code = pytesseract.image_to_string(image)  # 读取里面的内容
    return code






if __name__=="__main__":
    path = 'validateCode.png'
    a = readImage(path)
    print(a)
    # 新建Image对象
    image = Image.open("validateCode.png")
    # 调用tesserocr的image_to_text()方法，传入image对象完成识别
    result = pytesseract.image_to_data(image)
    print(result)