import urllib.request
import cv2
import numpy as np
import os

def resize_image():
    img = cv2.imread("note.jpg")
    resized_image = cv2.resize(img, (30, 60))
    cv2.imwrite("note2.jpg",resized_image)

# 下载图片并存储
def store_raw_images():
    neg_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n04607869'
    #urls = urllib.request.urlopen(neg_images_link)
    neg_image_urls = urllib.request.urlopen(neg_images_link).read().decode()
    pic_num = 65

    #判断目录是否存在，不存在重新创建
    if not os.path.exists('pos'):
        os.makedirs('pos')

    for i in neg_image_urls.split('\n'):
        try:
            print(i) # 打印url地址
            # 从网络地址下载图片到本地，并重命名
            urllib.request.urlretrieve(i, "pos/"+str(pic_num)+".jpg")
            # 读取从本地目录图片，同时进行图片灰度转换
            img = cv2.imread("pos/"+str(pic_num)+".jpg",cv2.IMREAD_GRAYSCALE)
            # should be larger than samples / pos pic (so we can place our image on it)
            # 重新设置图片大小为 100*100
            print(img)
            resized_image = cv2.resize(img, (100, 100))
            # 把灰度转换、修改尺寸大小图片重新保存至原文件目录（覆盖）
            cv2.imwrite("pos/"+str(pic_num)+".jpg",resized_image)
            pic_num += 1
            
        except Exception as e:
            print(str(e))  

def find_uglies():
    match = False
    for file_type in ['neg']:
        for img in os.listdir(file_type):
            for ugly in os.listdir('uglies'):
                try:
                    current_image_path = str(file_type)+'/'+str(img)
                    ugly = cv2.imread('uglies/'+str(ugly))
                    question = cv2.imread(current_image_path)
                    if ugly.shape == question.shape and not(np.bitwise_xor(ugly,question).any()):
                        print('That is one ugly pic! Deleting!')
                        print(current_image_path)
                        os.remove(current_image_path)
                except Exception as e:
                    print(str(e))


def create_pos_n_neg():
    for file_type in ['neg']:        
        for img in os.listdir(file_type):
            if file_type == 'pos':
                line = file_type+'/'+img+' 1 0 0 50 50\n'
                with open('info.dat','a') as f:
                    f.write(line)
            elif file_type == 'neg':
                line = file_type+'/'+img+'\n'
                with open('bg.txt','a') as f:
                    f.write(line)




#store_raw_images()

#find_uglies()
create_pos_n_neg()

#read_local_image()
