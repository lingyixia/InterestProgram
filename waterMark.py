# coding:utf-8

# -------------------------------------------------------------------------------
# @Author        chenfeiyu
# @Name:         waterMark.py
# @Project       waterMark
# @Product       PyCharm
# @DateTime:     2020-1-4 20:14
# @Contact       chinachenfeiyu@outlook.com
# @Version       1.0
# @Description:给图片加水印
# REF:https://github.com/lingyixia/InterestProgram
# -------------------------------------------------------------------------------
# -*- coding: utf-8 -*-

from PIL import Image

if __name__ == '__main__':
    print('请输入源文件和水印文件路径,空格隔开:')
    image_path, water_mark_path = [str(i) for i in input().split()]
    origin_image = Image.open(image_path)
    # 创建底图
    target = Image.new(mode='RGBA', size=origin_image.size)
    # 打开装饰
    water_mark = Image.open(water_mark_path)
    water_mark_size = water_mark.size
    cut_size_l, cut_size_w = target.size[0] // 10, target.size[1] // 10
    multiple = 1
    while True:
        water_mark_size = tuple(map(lambda x: x // multiple, water_mark_size))
        if water_mark_size[0] < target.size[0] // 10 or water_mark_size[1] < target.size[1] // 10:
            break
        else:
            water_mark_size = water_mark.size
            multiple += 1
    water_mark = water_mark.resize(water_mark_size)
    r, g, b, a = water_mark.split()
    target.paste(origin_image, (0, 0))
    water_mark.convert("RGBA")
    target.paste(water_mark, (0, 0), mask=a)
    target.save("new.png")
