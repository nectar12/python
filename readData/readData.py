#!/bin/env python
# coding: utf-8
from PIL import Image

file_object = open('info_20160411.txt')

for line in file_object:
    information = eval(line)
   # print information['卡号类型']

    if information['卡号类型'] == '平面':
        name = information['文件名']
        name = name.replace("\\", '/')
        path = "/Users/weiru/work/bankCard/" + name;
        im = Image.open(path)

        text = information['文本级信息']
        #print text[0].keys()

        #print len(str(text[0].keys()))
        if len(str(text[0].keys())) > 16:
            chars = information['字符级信息']
            #print type(chars)
            for i in range(len(str(text[0].keys()))-4):
                if len(chars[0]) == len(str(text[0].keys()))-4:
                    label = chars[0][i].keys()
                    location = chars[0][i].values()
                    print label
                    print location
                elif len(chars) > 1:
                    if len(chars[1]) == len(str(text[0].keys()))-4:
                        label = chars[1][i].keys()
                        location = chars[1][i].values()
                        print label
                        print location
