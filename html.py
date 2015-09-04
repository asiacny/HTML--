#!/usr/bin/env python
# -*- coding=cp936 -*-
# Copyright (C) 2015 Yeoman Zhuang

"""
html get name,id and phone
use module re to find phone number and Id number
file name such as "xxx-----3702...902.html"
@author: Yeoman
"""

import os
import re
import sys
import shutil
import pyExcelerator
import Tkinter
import tkFileDialog

version = 7


def delete_gap_dir(di):
    if os.path.isdir(di):
        for d in os.listdir(di):
            delete_gap_dir(di + os.sep + d)

        if not os.listdir(di):
            os.rmdir(di)
            print('�Ƴ���Ŀ¼: ' + di)


class HTML():

    """docstring for HTML"""

    def __init__(self):
        self.curPath = os.getcwd()
        self.root = Tkinter.Tk()
        self.root.title(u"��ȡ�ļ�")
        self.entry = Tkinter.Entry(self.root, width=40)
        self.entry.pack(side=Tkinter.TOP, anchor="nw")
        button = Tkinter.Button(self.root, text=u"��Ŀ¼", command=self.callback)
        button.pack(side=Tkinter.TOP, anchor="nw")
        button_start = Tkinter.Button(
            self.root, text=u'��ʼ��ȡ', command=self.start)
        button_start.pack(side=Tkinter.TOP, anchor='nw')
        button_ = Tkinter.Button(self.root, text=u'�˳�', command=self.quit)
        button_.pack(side=Tkinter.RIGHT, anchor='nw')
        self.root.mainloop()

    def callback(self):
        self.entry.delete(0, Tkinter.END)  # ���entry���������
        # ����filedialogģ���askdirectory()����ȥ���ļ���
        filepath = tkFileDialog.askdirectory()
        self.curPath = filepath.encode('gbk')
        if filepath:
            self.entry.insert(0, filepath)  # ��ѡ��õ�·�����뵽entry����

    def quit(self):
        delete_gap_dir(self.curPath)
        self.root.destroy()

    def start(self):
        city_name = ['������', '�Ϻ���', '�����', '������', 'ʯ��ׯ��', '̫ԭ��', '���ͺ�����',
                     '��ɽ��', '��ͬ��', '��ͷ��', '�ػʵ���', '��Ȫ��', '�ں���', '������',
                     '������', '�����', '��̨��', '������', '���ױ�����', '������', '˷����',
                     'ͨ����', '�żҿ���', '������', '�����첼��', '�е���', '������',
                     '������˹��', '������', '������', '�����׶���', '�ȷ���', '�ٷ���',
                     '��ˮ��', '�˳���', '��������', '������',
                     '������', '���������', '������', '������', 'ĵ������', '��ƽ��', '��ɽ��',
                     '��ľ˹��', '��Դ��', '��˳��', '������', 'ͨ����', '��Ϫ��', '������',
                     '��ɽ��', '������', '������', '�׳���', '������', '�׸���', '��ԭ��',
                     'Ӫ����', '˫Ѽɽ��', '������', '��̨����', '������', '�绯��', '�̽���',
                     '�ں���', '������', '������', '��«����', '�Ͼ���', '������', '�Ϸ���',
                     '������', '�ϲ���', '������', '������', '������', '�ߺ���', '������',
                     '������', '�ൺ��', '������', '������', '������', 'Ȫ����', '�˴���',
                     '�Ͳ���', '������', '������', '������', '������', '������', '��ׯ��',
                     '������', '������', '��ɽ��', '������', '������', '��Ӫ��', '��ͨ��',
                     '������', '������', '������', '������', '��̨��', '���Ƹ���', '����',
                     'ͭ����', '������', '�Ž���', 'Ϋ����', '������', '������', '������',
                     '��ƽ��', '��������', '������', '�γ���', '̨����', '��ɽ��', '������',
                     'Ƽ����', '̩����', '������', '��ˮ��', '������', '������', '������',
                     '����', '��ɽ��', '������', 'ӥ̶��', '������', '̩����', '������',
                     '������', '��Ǩ��', '������', '������', '������', '�ĳ���', '������',
                     '������', '������', '������', '������', '֣����', '�人��', '��ɳ��',
                     '������', '��ʯ��', '������', '������', 'ʮ����', '��̶��', '������',
                     '������', '������', '������', '�˲���', '������', 'ƽ��ɽ��', '������',
                     '������', '������', '������', '�żҽ���', '������', '������', '������',
                     '�����', '�Ƹ���', '������', '�����', 'Т����', '¦����', '�����',
                     '������', '������', '����Ͽ��', '������', '������', '�ױ���', '������',
                     '�ܿ���', 'פ�����', '������', '������', '��Դ��', '������', '������',
                     '������', '������', '������', '������', '�麣��', '������', '��ͷ��',
                     '������', '��ɽ��', '������', '�ع���', '������', 'տ����', '������',
                     '������', '�����', '������', '������', 'ï����', '������', '������',
                     '��ɫ��', '÷����', '�ӳ���', '��β��', '������', '��Դ��', '���Ǹ���',
                     '������', '��Զ��', '��ݸ��', '��ɽ��', '������', '������', '�Ƹ���',
                     '�ɶ���', '������', '������', '������', '������', '����ˮ��', '��ͨ��',
                     '�Թ���', '������', '������', '��֦����', '��˳��', '��Ϫ��', '������',
                     '�ն���', '������', '��ɽ��', '��Ԫ��', '������', '������', '�ٲ���',
                     '�ڽ���', '��ɽ��', '������', '�˱���', '�ϳ���', '������', '�Ű���',
                     '�㰲��', '������', 'üɽ��', '������', '������', '������', '������',
                     '��³ľ����', '������', '��������', 'ʯ��ɽ��', '����������', '������',
                     '�����', '������', 'ͭ����', '������', '��ԭ��', 'μ����', '��ˮ��',
                     '������', '������', '��Ȫ��', '������', '��Ҵ��', '������', '������',
                     '�Ӱ���', '������', '������', '¤����', 'ƽ����', '������',
                     '����', '�Ϻ�', '���', '����', 'ʯ��ׯ', '̫ԭ', '���ͺ���',
                     '��ɽ', '��ͬ', '��ͷ', '�ػʵ�', '��Ȫ', '�ں�', '����', '����', '���',
                     '��̨', '����', '���ױ���', '����', '˷��', 'ͨ��', '�żҿ�',
                     '����', '�����첼', '�е�', '����', '������˹', '����', '����',
                     '�����׶�', '�ȷ�', '�ٷ�', '��ˮ', '�˳�', '������', '����',
                     '����', '�������', '����', '����', 'ĵ����', '��ƽ', '��ɽ',
                     '��ľ˹', '��Դ', '��˳', '����', 'ͨ��', '��Ϫ', '����',
                     '��ɽ', '����', '����', '�׳�', '����', '�׸�', '��ԭ',
                     'Ӫ��', '˫Ѽɽ', '����', '��̨��', '����', '�绯', '�̽�',
                     '�ں�', '����', '����', '��«��', '�Ͼ�', '����', '�Ϸ�',
                     '����', '�ϲ�', '����', '����', '����', '�ߺ�', '����',
                     '����', '�ൺ', '����', '����', '����', 'Ȫ��', '�˴�',
                     '�Ͳ�', '����', '����', '����', '����', '����', '��ׯ',
                     '����', '����', '��ɽ', '����', '����', '��Ӫ', '��ͨ',
                     '����', '����', '����', '����', '��̨', '���Ƹ�', '��',
                     'ͭ��', '����', '�Ž�', 'Ϋ��', '����', '����', '����',
                     '��ƽ', '������', '����', '�γ�', '̨��', '��ɽ', '����',
                     'Ƽ��', '̩��', '����', '��ˮ', '����', '����', '����',
                     '��', '��ɽ', '����', 'ӥ̶', '����', '̩��', '����',
                     '����', '��Ǩ', '����', '����', '����', '�ĳ�', '����',
                     '����', '����', '����', '����', '֣��', '�人', '��ɳ',
                     '����', '��ʯ', '����', '����', 'ʮ��', '��̶', '����',
                     '����', '����', '����', '�˲�', '����', 'ƽ��ɽ', '����',
                     '����', '����', '����', '�żҽ�', '����', '����', '����',
                     '���', '�Ƹ�', '����', '���', 'Т��', '¦��', '���',
                     '����', '����', '����Ͽ', '����', '����', '�ױ�', '����',
                     '�ܿ�', 'פ���', '����', '����', '��Դ', '����', '����',
                     '����', '����', '����', '����', '�麣', '����', '��ͷ',
                     '����', '��ɽ', '����', '�ع�', '����', 'տ��', '����',
                     '����', '���', '����', '����', 'ï��', '����', '����',
                     '��ɫ', '÷��', '�ӳ�', '��β', '����', '��Դ', '���Ǹ�',
                     '����', '��Զ', '��ݸ', '��ɽ', '����', '����', '�Ƹ�',
                     '�ɶ�', '����', '����', '����', '����', '����ˮ', '��ͨ',
                     '�Թ�', '����', '����', '��֦��', '��˳', '��Ϫ', '����',
                     '�ն�', '����', '��ɽ', '��Ԫ', '����', '����', '�ٲ�',
                     '�ڽ�', '��ɽ', '����', '�˱�', '�ϳ�', '����', '�Ű�',
                     '�㰲', '����', 'üɽ', '����', '����', '����', '����',
                     '��³ľ��', '����', '������', 'ʯ��ɽ', '��������', '����',
                     '���', '����', 'ͭ��', '����', '��ԭ', 'μ��', '��ˮ',
                     '����', '����', '��Ȫ', '����', '��Ҵ', '����', '����',
                     '�Ӱ�', '����', '����', '¤��', 'ƽ��', '����']

        nu = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-']

        curFile = []

        dstPath = self.curPath + os.sep + '������'
        for allFile in os.walk(self.curPath):
            for fileName in allFile[2]:
                if '������' not in allFile[0] and 'δ��ȡ' not in allFile[0] and'����' not in allFile[0]:
                    curFile.append(allFile[0] + os.sep + fileName)
        # curFile = os.listdir(curPath)
        result = open(self.curPath + os.sep + 'result.txt', 'w')

        xlsResult = pyExcelerator.Workbook()
        xlsResultSheet = xlsResult.add_sheet(u'���ż�¼')

        result.write('����,���֤,�绰,����\n')
        xlsResultSheet.write(0, 0, u'����')
        xlsResultSheet.write(0, 1, u'���֤')
        xlsResultSheet.write(0, 2, u'�绰')
        xlsResultSheet.write(0, 3, u'����')
        curNum = 0
        findNum = 1
        failNum = 0
        totalNum = 0
        noInfoNum = 0
        resultNum = 0
        sumNum = len(curFile)
        try:
            os.mkdir(self.curPath + os.sep + 'δ��ȡ')
        except:
            print('����δ��ȡ�ļ���ʧ��')
        try:
            os.mkdir(self.curPath + os.sep + '����')
        except:
            print('���������ļ���ʧ��')
        try:
            os.mkdir(self.curPath + os.sep + '������')
        except:
            print('�����������ļ���ʧ��')
        for files in curFile:
            curNum += 1
            print(str(curNum) + '/' + str(sumNum) + '\r'),
            flag = 0
            contains = (files.find('.htm') >= 0)  # and(files.find('-') >= 0)
            if contains:
                i = 0
                tempFile = os.path.split(files)[1]
                while (tempFile[i] not in nu) and (tempFile[i] != '.'):
                    i += 1
                Id = re.search(r'\d{17}[\dX]', tempFile)
                File = open(files)
                lines = File.readlines()
                phone = ''
                if len(lines) > 394:
                    if flag == 0:
                        m = re.search(r'>0?1(3|4|5|6|7|8)\d{9}<', lines[245])
                        if m:
                            flag = 1
                            phone = m.group(0)[-12:-1]
                    if flag == 1:
                        for line in lines[270], lines[273], lines[378], lines[393]:
                            for c in city_name:
                                if c in line and flag == 1:
                                    city = c
                                    flag = 2
                                    break
                            if flag == 2:
                                break
                    if flag != 2:
                        for line in lines:
                            if m:
                                flag = 1
                                phone = m.group(0)[-12:-1]
                            else:
                                m = re.search(r'>0?1(3|4|5|6|7|8)\d{9}<', line)
                            if flag == 1:
                                for c in city_name:
                                    if c in line:
                                        flag = 2
                                        city = c
                                        break
                                if flag == 2:
                                    break
                            if flag == 2:
                                break
                    if flag == 2:
                        result.write(tempFile[:i] + ",")
                        if Id:
                            result.write(Id.group(0) + ",")
                            xlsResultSheet.write(findNum, 1, Id.group(0))
                        else:
                            result.write(",")
                        result.write(phone + ",")
                        result.write(city + "\n")
                        xlsResultSheet.write(
                            findNum, 0, tempFile[:i].decode('gbk'))
                        xlsResultSheet.write(findNum, 2, phone)
                        xlsResultSheet.write(
                            findNum, 3, city.decode('gbk'))
                        findNum += 1
                        try:
                            os.mkdir(dstPath + os.sep + city)
                        except:
                            pass
                        try:
                            shutil.copy(files, dstPath + os.sep + city)
                        except:
                            # os.remove(files)
                            failNum += 1
                            resultNum += 1
                File.close()
                if flag == 0:
                    try:
                        shutil.copy(files, self.curPath + os.sep + 'δ��ȡ')
                    except:
                        # os.remove(files)
                        failNum += 1
                        noInfoNum += 1
                try:
                    shutil.move(files, self.curPath + os.sep + '����')
                except:
                    os.remove(files)
                    failNum += 1
                    totalNum += 1

        result.close()
        xlsResult.save(self.curPath + os.sep + 'result.xls')

        print('������ϣ�')
        print('��' + str(sumNum) + '��html�ļ����ɹ���ȡ' + str(curNum) + '���ļ�')
        print('����' + str(failNum) + '���ļ��ظ����ƶ�ʧ��')
        print('����' + str(resultNum) + '���ļ��ڷ��������ظ�'),
        print(str(noInfoNum) + '���ļ���δ��ȡ���ظ�'),
        print(str(totalNum) + '���ļ��ڼ������ظ�')

test = HTML()
