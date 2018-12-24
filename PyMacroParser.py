# coding=utf-8
import math
import sys
import os


def dealwithComments(inputs):
    '''
    作为load的调用函数
    将空格以及空行进行转义
    :param 输入的是源文件内容，第一步处理cpp注释，包括空白注释行以及
    :return:返回列表
    '''
    outputs = []
    flag_quot = False
    block_comment = False
    input_length = len(inputs)
    for i in range(input_length):
        c = inputs[i]
        if c == '\"':
            if i == 0 or inputs[i - 1] != '\\':
                if not block_comment:
                    flag_quot = not flag_quot
        elif i < input_length - 1 and c == '/' and inputs[i + 1] == '*' and not block_comment:
            if not flag_quot:
                block_comment = True
        elif i >= 1 and inputs[i - 1] == '*' and c == '/' and block_comment:
            block_comment = False
            continue

        if not block_comment:
            outputs.append(c)

    flag_quot2 = False
    line_comment = False
    for i in range(input_length):
        c2 = inputs[i]
        if c2 == '\"':
            if i == 0 or inputs[i - 1] != '\\':
                if not line_comment:
                    flag_quot2 = not flag_quot2
        elif i < input_length - 1 and c2 == '/' and inputs[i + 1] == '/' and not line_comment:
            if not flag_quot2:
                line_comment = True
        elif c2 == '\n' and line_comment:
            if not flag_quot2:
                line_comment = False
        if not line_comment:
            outputs.append(c2)


    lines = ''.join(outputs).split('\n')

    for one_line in lines:
        if one_line:
            for i in one_line.strip():
                outputs.append(i)
            outputs.append('\n')
    outputs = outputs[:-1]

    flag_ignore = False
    temp_space = []
    for i in outputs:
        if i == '#' and not flag_ignore:
            flag_ignore = True
            temp_space.append(i)
        elif i in '\t' and flag_ignore:
            continue
        elif c != ' ' and flag_ignore:
            flag_ignore = False
            temp_space.append(i)
        else:
            temp_space.append(i)



def dealwithBlockLines():
    '''
    同样作为load调用的函数
    首先调用dealwithComments处理掉注释，然后调用该函数处理掉空行
    :return:返回列表
    '''

class PyMacroParser(object):
    def __init__(self):
        this_dict = {

        }

        output = []
        pass




    def load(self,f):   #其中f为文件路径，有两种异常跑出的方式
        '''

        :param f:
        :return:

        with open(f,'r') as sourceFile:
            inputs = sourceFile.read()
            要求要有异常处理，with open语句貌似不好跑出异常
        '''
        try:
            sourceFile = open(f,'r')
            raw_inputs = sourceFile.read()
            self.output = dealwithComments(raw_inputs)
            print self.output
        except IOError,e:
            print 'read IOError!!!',e
        finally:
            if sourceFile:
                sourceFile.close()


        pass

    def preDefine(self,s):
        pass

    def dumpDict(self):
        pass
        return dict

    def dump(self,f):
        pass

if __name__ == "__main__":
    file = 'origin.cpp'
    a1 = PyMacroParser()
    a1.load(file)
