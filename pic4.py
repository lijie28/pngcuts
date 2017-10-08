# -*- coding:utf-8 -*-
from PIL import Image


def resize_image(img_path):
    try:
        mPath, ext = os.path.splitext(img_path)
        if astrcmp(ext, ".png") or astrcmp(ext, ".jpg"):
            img = Image.open(img_path)
            (width, height) = img.size

            if width != new_width:
                new_height = int(height * new_width / width)
                out = img.resize((new_width, new_height), Image.ANTIALIAS)
                new_file_name = '%s%s' % (mPath, ext)
                out.save(new_file_name, quality=100)
                Py_Log("图片尺寸修改为：" + str(new_width))
            else:
                Py_Log("图片尺寸正确，未修改")
        else:
            Py_Log("非图片格式")
    except Exception, e:
        print e


def printFile(dirPath):
    print "file: " + dirPath
    resize_image(dirPath)
    return True


if __name__ == '__main__':
    path = "E:\pp\icon_setting.png"
    new_width = 50
    try:
        b = printFile(path)
        Py_Log("\r\n          **********\r\n" +
               "*********图片处理完毕*********" + "\r\n          **********\r\n")
    except:
        print "Unexpected error:", sys.exc_info()


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
