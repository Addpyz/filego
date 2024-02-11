import sys

m = sys.argv[1]

print("主程序")
print("________")
print("!@~#$%^&*(){}:;'|~>?<")

if m == 'play':   
    from play import*
elif m=='self':
    from self import*
elif m=='copysgf':
    from copysgf import*  
elif m=='sgf2json':
    from sgf2json import*
else:
    print("暂时没有该功能")
