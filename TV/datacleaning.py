# -*- coding:utf-8 -*-
import csv
import sys
import re
import webbrowser
reload(sys)
#import webbrowser
sys.path.append("libs")
sys.setdefaultencoding("utf-8")

with open('tv.csv','r+') as csvfile:#主要是将原csv文件中的第2,3列数据进行清洗，去除多余的字符，只保留数字
    reader = csv.reader(csvfile)
    rows=[]#经过处理的数据放在这里
    for r1,r2,r3,r4 in reader:
        try:#主要是因为第一行是标题，不是内容
            r2=int(filter(lambda ch: ch in '0123456789', str(r2)))
            r3=int(filter(lambda ch: ch in '0123456789', str(r3)))
        except BaseException, e:#这个应该写啥我也没搞懂，反正不需要
            continue
        else:
            row=[r1,r2,r3,r4]
            rows.append(row)

with open('tv_cleaned.csv','wb') as csvfile:
	writer = csv.writer(csvfile)
	a=0
	while a < len(rows):
		writer.writerow(rows[a])
		a=a+1


