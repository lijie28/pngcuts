# -*- coding:utf-8 -*-

import os  
  

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

# print dirlist(os.path.dirname(os.path.realpath(__file__)), []) 
'''

def file_name(file_dir):   
# 先输入文件夹路径，编历当前文件夹下的所有文件（取出路径，返回数组）
    all_files = []
    for root, dirs, files in os.walk(file_dir):  
        # print(root) #当前目录路径  
        # print(dirs) #当前路径下所有子目录  
        # print(files) #当前路径下所有非目录子文件  
        all_files = files
    return all_files  


def splitit(name_list):
# 取出文件名及后缀(返回数组)
    new_list = []
    for a in name_list:
        new_list.append(os.path.splitext(a))
    return new_list


print splitit(file_name(os.path.dirname(os.path.realpath(__file__))))

# 判断文件是否png，是的话输出图片大小，不是的话抛出文件名及后缀

# 将png文件大小改成对应尺寸，并重全名导出
