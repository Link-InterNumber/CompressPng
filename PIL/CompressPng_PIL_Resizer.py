import getopt
import math
import os
import os.path
import sys
from tkinter import filedialog

from PIL import Image


# 压缩图片
def reducePic(srcFile: str, dstFile):
    img_name = srcFile.split('\\')[-1]
    pth = srcFile.replace('/', '\\')
    print('img_name:' + img_name)
    print('pth:' + srcFile)
    png_pil = Image.open(srcFile, mode="r")
    size = png_pil.size
    if size[0] <= 4 or size[1] <= 4:
        return
    if size[0] <= 20 and size[1] <= 20:
        return
    newWidth = math.ceil(size[0] / 4) * 4
    newheight = math.ceil(size[1] / 4) * 4
    png_pil = png_pil.resize((newWidth, newheight))
    png_pil.save(pth, "png", quality=0, optimize=True, compress_level=9)



# 循环递归遍历文件夹
def traverse(file_dir):
    fs = os.listdir(file_dir)
    for dir in fs:
        tmp_path = os.path.join(file_dir, dir)
        if not os.path.isdir(tmp_path):
            tu = os.path.splitext(tmp_path)
            # print(tmp_path)
            if tu[1] in g_reduceFileExt:
                newPath = tmp_path.replace(g_srcPath, g_dstPath)
                # print(newPath)
                reducePic(tmp_path, newPath)
        else:
            # createFloder(tmp_path.replace(g_srcPath, g_dstPath))
            traverse(tmp_path)


def getFloderPath():
    opts, args = getopt.getopt(sys.argv[1:], "p:s:")
    file_path = ""
    for op, value in opts:
        if op == "-p":
            file_path = value
    return file_path


def createFloder(dstpath):
    if not os.path.exists(dstpath):
        os.mkdir(dstpath)


def main():
    # 当前路径
    global g_curDir
    g_curDir = os.path.dirname(os.path.realpath(__file__))
    # g_curDir = g_curDir.replace('/', '\\')
    # os.path.dirname(os.path.realpath(__file__))

    # 需要压缩的图片扩展名
    global g_reduceFileExt
    g_reduceFileExt = ['.png']
    # 压缩后的图片存储目录
    global g_dstPath
    g_dstPath = g_curDir
    # createFloder(g_dstPath)

    global g_srcPath
    g_srcPath = filedialog.askdirectory()
    print('g_srcPath: ' + g_srcPath)
    traverse(g_srcPath)
    print('files reduce success')
    input(r'Press any key to quit.')


if __name__ == '__main__':
    main()
