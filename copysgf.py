import os
import sys

# 获取目录路径
path = sys.argv[1] if len(sys.argv) > 1 else './'

# 打开输出文件
out = open(os.path.join(path, 'file.sgf'), 'w')

# 遍历目录下的所有文件
sgfs = ''
files = os.listdir(path)
for file in files:
    if file.endswith('.sgf'):  # 检查文件扩展名
        with open(os.path.join(path, file), 'rb') as f:  # 使用完整路径打开文件
            data = f.read()
            sgfs += data.decode('utf-8','ignore')  # 在文件内容之间添加分隔符

# 写入合并后的内容到输出文件
out.write(sgfs)
out.close()
