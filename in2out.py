def strlip(data):
    lst = data[2:]
    return lst
def to_s(data):
    x = data[0]
    if ord(x)>=73:
        x = ord(x)+32
        x = chr(x)
    else:
        x = chr(ord(x)+32)
    return x
def to_n(data):
    y = data[1:]
    y = int(y)
    nmap = {
    's': 1,
    'r': 2,
    'q': 3,
    'p': 4,
    'o': 5,
    'n': 6,
    'm': 7,
    'l': 8,
    'k': 9,
    'j': 10,
    'i': 11,
    'h': 12,
    'g': 13,
    'f': 14,
    'e': 15,
    'd': 16,
    'c': 17,
    'b': 18,
    'a': 19,
}
    key_list=list(nmap.keys())
    val_list=list(nmap.values())
    vid = val_list.index(y)
    kid = key_list[vid]
    return kid
def main(data):
    dat = strlip(data)
    da = data[0]+'['+to_s(dat)+to_n(dat)+']'
    return da
if __name__ == '__main__':
    t = input()
    print(main(t))
    
    
