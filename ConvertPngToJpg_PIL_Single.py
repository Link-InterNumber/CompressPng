import os.path
import sys

from PIL import Image


# 压缩图片
def reducePic(srcFile: str):
    img_name = srcFile.split('\\')[-1]
    pth = srcFile.replace('/', '\\')
    print('img_name:' + img_name)
    print('pth:' + srcFile)
    png_pil = Image.open(srcFile, mode="r")
    # if png_pil.mode == 'RGBA':
    #     return
    # png_pil.save(pth, "PNG", quality=45, optimize=True)
    # # 如果对质量要求再低些，
    # # 渐变的地方会出现失真
    try:
        out_pil = png_pil.convert(mode="RGB")
        # out_pil = out_pil.convert(mode="RGBA", dither=Image.FLOYDSTEINBERG, palette=Image.ADAPTIVE, colors=256)
        # out_pil.filter(ImageFilter.ModeFilter(20))
        new_file = os.path.splitext(srcFile)[0] + '.jpg'
        out_pil.save(new_file, quality=100, optimize=True, compress_level=0)
    except Exception as r:
        print('未知错误 %s' % (r))
        png_pil.save(pth, "PNG", quality=0, optimize=True, compress_level=9)


# # 循环递归遍历文件夹
# def traverse(file_dir):
#     fs = os.listdir(file_dir)
#     for dir in fs:
#         tmp_path = os.path.join(file_dir, dir)
#         if not os.path.isdir(tmp_path):
#             tu = os.path.splitext(tmp_path)
#             # print(tmp_path)
#             if tu[1] in g_reduceFileExt:
#                 newPath = tmp_path.replace(g_srcPath, g_dstPath)
#                 # print(newPath)
#                 reducePic(tmp_path)
#         else:
#             # createFloder(tmp_path.replace(g_srcPath, g_dstPath))
#             traverse(tmp_path)


# def getFloderPath():
#     opts, args = getopt.getopt(sys.argv[1:], "p:s:")
#     file_path = ""
#     for op, value in opts:
#         if op == "-p":
#             file_path = value
#     return file_path
#
#
# def createFloder(dstpath):
#     if not os.path.exists(dstpath):
#         os.mkdir(dstpath)
#
#
# def main():
#     # 当前路径
#     global g_curDir
#     g_curDir = os.path.dirname(os.path.realpath(__file__))
#     # g_curDir = g_curDir.replace('/', '\\')
#     # os.path.dirname(os.path.realpath(__file__))
#
#     # 需要压缩的图片扩展名
#     global g_reduceFileExt
#     g_reduceFileExt = ['.png', '.jpg']
#     # 压缩后的图片存储目录
#     global g_dstPath
#     g_dstPath = g_curDir
#     # createFloder(g_dstPath)
#
#     global g_srcPath
#     g_srcPath = filedialog.askdirectory()
#     print('g_srcPath: ' + g_srcPath)
#     traverse(g_srcPath)
#     print('files reduce success')
#     input(r'Press any key to quit.')


if __name__ == '__main__':
    # main()
    g_reduceFileExt = ['.png']
    pngPath = sys.argv[1]
    tu = os.path.splitext(pngPath)
    if tu[1] in g_reduceFileExt:
        reducePic(pngPath)
    print('files converted success')
    input(r'Press any key to quit.')
