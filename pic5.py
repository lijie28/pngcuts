# encoding=utf-8
# author: walker
# date: 2014-05-15
# function: 更改图片尺寸大小
import os
import os.path
from PIL import Image
'''
filein: 输入图片
fileout: 输出图片
width: 输出图片宽度
height:输出图片高度
type:输出图片类型（png, gif, jpeg...）
'''


def ResizeImage(filein, fileout, width, height, type):
    img = Image.open(filein)
    # resize image with high-quality
    out = img.resize((width, height), Image.ANTIALIAS)


    out.save(fileout, type)


if __name__ == "__main__":
    filein = r'test.png'
        
        
    fileout = r'icon/%s' % 'testout1111.png'
    # fileout = r'icon/testout1111.png'

    width = 60
    height = 85
    type = 'png'
    ResizeImage(filein, fileout, width, height, type)
    print '成功',fileout

def BFS_Dir(dirPath, dirCallback=None, fileCallback=None):
    queue = []
    ret = []
    queue.append(dirPath)
    while len(queue) > 0:
        tmp = queue.pop(0)
        if os.path.isdir(tmp):
            ret.append(tmp)
            for item in os.listdir(tmp):
                queue.append(os.path.join(tmp, item))
            if dirCallback:
                dirCallback(tmp)
        elif os.path.isfile(tmp):
            ret.append(tmp)
            if fileCallback:
                fileCallback(tmp)
    return ret
