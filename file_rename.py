
import os


'''
1. 读取目录下所有文件并重新命名
2. 只修改.jpg 结尾的图片名称
'''

def rename_file():

    # 定义目录
    path = '/Users/wesley/PycharmProjects/Deeplearn/Opencv_traincascade/test/'
    # 获取目录下文件名
    dir = os.listdir(path)
    # 设置初始名
    pic_num = 0

    # 主体
    for i in dir:
        # 打印文件原名
        print('Old File Name : {0}'.format(i))
        file_filter = os.path.join(path, i)
        # 判断过滤以 .jpg 结尾的文件
        if file_filter.endswith('.jpg'):
                # 新文件名
                newname = str(pic_num) + ".jpg"
                # 重命名为新文件名
                os.rename(file_filter, os.path.join(path, newname))
                print('New File Name : {0}'.format(newname))

        pic_num += 1

if __name__ == "__main__":
    rename_file()
