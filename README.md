# CompressPng
收集的数种免费png压缩算法，利用python编写批量处理工具

1、pngquant：
  最快、压缩率最高的有损压缩工具，将文件夹拖到CompressPng_Pngquant_DrawFoldHereToCompress.bat上放开即可压缩。

2、OpenCv：
  使用python内的OpenCv（cv2）库，选择文件夹即可对文件夹内的图片进行压缩，图片压缩功能太垃圾了。

3、PIL：
  使用python内的pillow库将png转换为8bit，速度快，压缩率80%左右，但图片会有明显失真。

4、optipng：
  无损压缩，压缩率在10~25%左右，速度较慢。

5、pngout：
  无损压缩，压缩率比optipng低，速度较快。

6、zopflipng：
  压缩率最高的无损压缩，也是速度最慢，需要用多线程提高效率。
