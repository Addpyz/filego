#导入库
import json
import os
import re
#目录路径
path = "./"
#将文件夹中的所有文件名转为列表
files = os.listdir(path) 
#定以一个标记
n = 0
#output用于储存
output = ''
#遍历文件名
for file in files:
    #检查文件是否为.sgf文件
    if file.endswith('.sgf'):
        n += 1
        #删除原有后缀，并将删除后的文件名储存至变量
        suffix = file.split('.')[0]
        #打开源文件
        with open(file, 'r')as f:
            #将文件中所有内容储存
            data = f.read()
            #储存
            d1 = re.findall(r'B\[[a-zA-Z]{2}\]', data)
            d2 = re.findall(r'W\[[a-zA-Z]{2}\]', data)
            x = dict(zip(d1,d2))
            output += json.dumps(x)
        #条件
        if n%5 == 0:
            fw = open('file'+str(n)+'.json', 'w')
            json.dump(output, fw)
            fw.close()
            output = ''
        print(file)
#处理剩余sgf的
if output != '':
    fw = open('file' + str(n+1) + '.json', 'w')  # 假设n已经更新为处理到最后一个文件的索引
    json.dump(output, fw)
    fw.close()
    output = ''
#删除文件
for file in files:
    if file.endswith('.sgf'):
       os.remove(file)
input("okk")       
