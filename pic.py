# -*- coding:utf-8 -*-

import os
from PIL import Image


'''
def dirlist(path, allfile):  
# 先输入文件夹路径，编历当前文件夹下的所有文件（取出路径，返回数组）
    filelist =  os.listdir(path)  
  
    for filename in filelist:  
        filepath = os.path.join(path, filename)  
        if os.path.isdir(filepath):  
            dirlist(filepath, allfile)  
        else:  
            allfile.append(filepath)  
    return allfile  

# print "os.path.dirname(os.path.realpath(__file__))=%s" % os.path.dirname(os.path.realpath(__file__))

print dirlist(os.path.dirname(os.path.realpath(__file__)), []) 
'''


file_path = os.getcwd() + '/icon/'
print file_path
if not os.path.exists(file_path):
    os.makedirs(file_path)
    
def file_name(file_dir):
    # 先输入文件夹路径，编历当前文件夹下的所有文件（取出路径，返回数组）
    all_files = []
    i = 0
    for root, dirs, files in os.walk(file_dir):
        # print(root) #当前目录路径
        # print(dirs) #当前路径下所有子目录
        # print "第%d个\nfiles:%s\n"%(i,files)
        if i == 0:
            all_files = files
        i = i + 1
    return all_files


def splitit(name_list):
    # 取出文件名及后缀(返回数组)
    new_list = []
    for name in name_list:
        new_list.append(os.path.splitext(name))
    return new_list


# print os.path.dirname(os.path.realpath(__file__))
newl = splitit(file_name(os.path.dirname(os.path.realpath(__file__))))


def judge_png(split_list):
    # 判断文件是否png，是的话输出图片大小，不是的话抛出文件名及后缀
    is_png = []
    is_not_png = []
    i = 0
    for the_one in split_list:
        if the_one[1] == '.png':

            strT = ''.join(the_one)
            is_png.append(strT)
            img = Image.open(strT)

            print '(', i, ')', strT, img.size
            i = i + 1

        else:
            strT = ''.join(the_one)
            is_not_png.append(strT)
    return(is_png, is_not_png)



def ResizeImage(filein, fileout, width, height):
    img = Image.open(filein)
    # resize image with high-quality
    out = img.resize((width, height), Image.ANTIALIAS)
    out.save(fileout, 'png')
    print '保存'

def AddDesc(oname,desc):
    #名字在后缀前加@2x,@3x
    n_list = os.path.splitext(oname)
    strT = n_list[0] + desc + n_list[1]
    # print n_list ,strT
    return strT


def get_new_png(is_png, is_not_png):
    # 将png文件大小改成对应尺寸，并重全名导出
    print "其中有%d个不是png:\n%s\n" % (len(is_not_png), is_not_png)

    # 获取到当前文件的目录，并检查是否有report文件夹，如果不存在则自动新建report文件
    # print '创立成功'
    for pic in is_png:

        img = Image.open(pic)

        pic_in =  pic
        pic_out_3x = 'icon/%s' % AddDesc(pic,'@3x')
        width_3x = img.size[0]
        height_3x = img.size[1]
        ResizeImage (pic_in,pic_out_3x,width_3x,height_3x)


        pic_out_2x = 'icon/%s' % AddDesc(pic,'@2x')
        width_2x = int(width_3x*750/1242)
        height_2x = int(height_3x*1334/2208)
        ResizeImage (pic_in,pic_out_2x,width_2x,height_2x)

        print '成功创建',pic_out_3x
        # img = Image.open(pic)
        # print(img.size)


a = judge_png(newl)
get_new_png(a[0], a[1])
