#!/bin/env python
# coding: utf-8
from PIL import Image

file_object = open('info_20160411_1.txt')
workPath = "/Users/weiru/work/bankCard/"

for line in file_object:
    information = eval(line)
   # print information['卡号类型']
    if information['卡号类型'] == '平面':
        name = information['文件名']
        name = name.replace("\\", '/')
        imgPath = workPath + name
        img = Image.open(imgPath)
        disPath = workPath + "bankcard_2000/plain/"
        name = name.replace('/', '_')
        text = information['文本级信息']
        #print text[0].keys()
        chars = information['字符级信息']
        #print len(str(text[0].keys()))
        if len(str(text[0].keys())) > 16:
            flag0 = [0, 0]
            for i in range(len(str(text[0].keys()))-4):
                if len(chars) > 1:
                    if len(chars[0]) == len(str(text[0].keys()))-4:
                        label = chars[0][i].keys()[0]
                        location = chars[0][i].values()
                        #print label
                        location = map(eval, location[0])
                        location = tuple(location)
                        #cropImg = img.crop(location)
                        #savePath = disPath + label + "/" + label + '_' + name[14:]
                        #cropImg.save(savePath)
                    elif len(chars[1]) == len(str(text[0].keys()))-4:
                        label = chars[1][i].keys()[0]
                        location = chars[1][i].values()
                        #print label
                        location = map(eval, location[0])
                        location = tuple(location)
                        #cropImg = img.crop(location)
                        #savePath = disPath + label + "/" + label + '_' + name[14:]
                        #cropImg.save(savePath)
                    else:
                        if flag0[0] == 0:
                            print name + '\t' + 'error1'
                            flag0[0] = 1
                else:
                    if len(chars[0]) == len(str(text[0].keys()))-4:
                        label = chars[0][i].keys()[0]
                        location = chars[0][i].values()
                        #print label
                        location = map(eval, location[0])
                        location = tuple(location)
                        #cropImg = img.crop(location)
                        #savePath = disPath + label + "/" + label + '_' + name[14:]
                        #cropImg.save(savePath)
                    else:
                        if flag0[1] == 0:
                            print name + '\t' + 'error2'
                            flag0[1] = 1
        elif (len(text) > 1) and (len(str(text[1].keys())) > 16):
            flag1 = [0, 0]
            for i in range(len(str(text[1].keys()))-4):
                if len(chars) > 1:
                    if len(chars[0]) == len(str(text[1].keys()))-4:
                        label = chars[0][i].keys()[0]
                        location = chars[0][i].values()
                        #print label
                        location = map(eval, location[0])
                        location = tuple(location)
                        #cropImg = img.crop(location)
                        #savePath = disPath + label + "/" + label + '_' + name[14:]
                        #cropImg.save(savePath)
                    elif len(chars[1]) == len(str(text[1].keys()))-4:
                        label = chars[1][i].keys()[0]
                        location = chars[1][i].values()
                        #print label
                        location = map(eval, location[0])
                        location = tuple(location)
                        #cropImg = img.crop(location)
                        #savePath = disPath + label + "/" + label + '_' + name[14:]
                        #cropImg.save(savePath)
                    else:
                        if flag1[0] == 0:
                            print name + '\t' + 'error3'
                            flag1[0] = 1
                else:
                    if len(chars[0]) == len(str(text[1].keys()))-4:
                        label = chars[0][i].keys()[0]
                        location = chars[0][i].values()
                        #print label
                        location = map(eval, location[0])
                        location = tuple(location)
                        #cropImg = img.crop(location)
                        #savePath = disPath + label + "/" + label + '_' + name[14:]
                        #cropImg.save(savePath)
                    else:
                        if flag1[1] == 0:
                            print name + '\t' + 'error4'
                            flag1[1] = 1
        else:
            print name + '\t' + 'error5'
