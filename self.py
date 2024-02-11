import random  
import os  
import sys  
  
def luoz(a):  
    r = 1  
    output = ""  # 新增一个变量用于保存输出结果  
    while r < 350:  
        a = "abcdefghijklmnopqrst"  
        l = random.choice(a)  
        m = random.choice(a)  
        z = random.choice(a)  
        k = random.choice(a)  
        for letter in l:  
            output += ";B[" + m + letter + "]" + ";" + "W[" + z + k + "] "  # 将结果添加到output变量中  
        r += 1  
    return output  # 返回输出结果  
  
x = int(input("请输入生成棋谱数量:"))  
b = sys.argv[1] if len(sys.argv) > 1 else "file"  # 默认使用"file"作为文件名前缀  

dirs = b
if not os.path.exists(dirs):
    os.makedirs(dirs)
  
sz = int(input("棋盘路数(19/13/9)\n"))
for i in range(1, x + 1):    
    file_name = f"{b}{i}.sgf"    
    with open(file_name, 'w') as file:  
        if sz==19:
            luoz_output = luoz("abcdefghijklmnopqrst")
            file.write("(SZ[19]")
        elif sz==13:
            luoz_output = luoz("abcdefghijklmn")
            file.write("(SZ[13]")
        elif sz==9:
            louz_output = luoz("abcdefghij")
            file.write("(SZ[9]")        
        else:
            print("没有这个路数")
        file.write(str(luoz_output) + ")\n")  
    print("generated "+str(i)+" file")
print("Finished")
  
input()
