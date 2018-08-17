import os
import cv2 as cv


'''
1. 读取目录下文件
2. 转换图片为灰色
3. 设置图片大小为 64*64

'''

def img_convert():

    # 图片存储目录
    path = '/Users/wesley/PycharmProjects/Deeplearn/Opencv_traincascade/info/'
    # 获取目录下文件名
    get_file_name = os.listdir(path)
    pic_num = 0

    for i in get_file_name:

        file_tpye = os.path.join(path, i)
        if file_tpye.endswith('.png') == True:
            print(i)
            img_url = str(path+i)
            # 从指定目录读取文件并灰度
            img_convert = cv.imread(img_url, cv.IMREAD_GRAYSCALE)
            # 设置图片大小
            img_resize = cv.resize(img_convert, (50, 50))
            # 把灰度、重置大小后的图片覆盖原文件
            cv.imwrite(img_url, img_resize)

    pic_num += 1


if __name__ == "__main__":
    img_convert()