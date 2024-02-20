#!/usr/bin/python
# -*- coding:UTF-8 -*-

import os, os.path
import sys, getopt
from tkinter import filedialog


# 压缩图片
def reducePic(srcFile, dstFile):
    # srcFile = srcFile.replace('\\', '/')
    cmd = g_curDir + '\\optipng.exe -o7 %s' % srcFile
    os.system(cmd)


# 循环递归遍历文件夹
def traverse(file_dir):
    fs = os.listdir(file_dir)
    for dir in fs:
        tmp_path = os.path.join(file_dir, dir)
        if not os.path.isdir(tmp_path):
            tu = os.path.splitext(tmp_path)
            print(tmp_path)
            if tu[1] in g_reduceFileExt:
                newPath = tmp_path.replace(g_srcPath, g_dstPath)
                print(newPath)
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
    g_reduceFileExt = ['.png', '.jpg']
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
