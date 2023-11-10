import getopt
import multiprocessing
import os
import os.path
import sys
from tkinter import filedialog

from zopflipng import png_optimize
from multiprocessing.pool import Pool


# 压缩图片
def reducePic(srcFile: str):
    img_name = srcFile.split('\\')[-1]
    pth = srcFile.replace('/', '\\')
    print('img_name:' + img_name)
    print('pth:' + pth)
    data = open(pth, 'rb').read()
    result, code = png_optimize(data)
    # result, code = png_optimize(data, lossy_8bit=True, lossy_transparent=True, num_iterations=500)
    # if code ==0 ,png compression success
    if code == 0:
        # save png
        with open(pth, 'wb') as f:
            f.write(result)
            f.close()
    print(img_name + ' was compressed.')


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
                path_list.append(tmp_path)
                # reducePic(tmp_path, newPath)
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
    # print('g_srcPath: ' + g_srcPath)
    traverse(g_srcPath)


if __name__ == '__main__':
    multiprocessing.freeze_support()
    path_list = []
    main()
    print('wait for compressing count: %d' % len(path_list))
    pool = Pool(5)
    for p in path_list:
        pool.apply_async(reducePic, (p,))
    # pool.imap(reducePic, path_list, 128)
    pool.close()
    pool.join()
    print('files reduce success')
    input(r'Press any key to quit.')
