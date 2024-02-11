#导入库
import os
import sys
import datetime
import re
import out2in as out2
import in2out as in2
from ais import* 

#读取文件
file = sys.argv[1] if len(sys.argv) > 1 else "file.sgf"
sgf = open(file, 'r')
data = sgf.read()
sgf.close()

#获取落子
p = r'B\[[a-zA-Z]{2}\]|W\[[a-zA-Z]{2}\]'
data_list = re.findall(p, data)

#选择黑白
print("请选择黑白(黑按1，白按2，人数按ad)")
choose = int(input())
 
#对弈 
def play(filename, l):
    p = r'B\[[a-zA-Z]{2}\]|W\[[a-zA-Z]{2}\]'
    output = ""
    r = 0
    global data_list
    history = []
    while r<=200:
        with open(filename, 'a+')as f:
            if r==0:
                f.write('(;)'+str(l)+';')
            content = f.read()        
            man = input("请落子：")
            player = in2.main(man)
            if len(re.findall(p, player))==1:
                if player not in data_list:
                    print("棋谱中没有这一手")
                    input()
                    break
                playw = ais(data_list, player)
                if playw  not in history and player not in history:
                    playwer = out2.main(playw)
                    print(history, player, playwer)
                    output = player+';'+ playw+';'+')'
                    f.write(output)

            r += 1
            

filename = datetime.datetime.now().strftime("%Y%m%d%H%M")+".sgf"  
mode = 'w' if choose == 1 else 'a'

# 如果是以追加模式打开的（即choose != 1），这里可以追加一个结束符号，以便于区分不同的游戏记录
if mode == 'a':
    print(data_list[0])
    play(filename, data_list[0])
else:
    play(filename, '')

print(f"游戏记录已保存到 {filename} 文件中。")
