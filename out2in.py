def strlip(input_string):
    start_index = input_string.find('[')
    end_index = input_string.find(']')
    if start_index != -1 and end_index != -1 and start_index < end_index:
        return input_string[start_index + 1:end_index]  

def to_uppercase(char):
    s = ord(char)
    if s >= 105:
        char = chr(s-31)
    else:
        char = chr(s-32)
    return char
        


def xyt(xy):
  column_map = {
    't': 1,
    's': 2,
    'r': 3,
    'q': 4,
    'p': 5,
    'o': 6,
    'n': 7,
    'm': 8,
    'l': 9,
    'k': 10,
    'j': 11,
    'h': 12,
    'g': 13,
    'f': 14,
    'e': 15,
    'd': 16,
    'c': 17,
    'b': 18,
    'a': 19,
}
  zuo = strlip(xy)
  lst = list(zuo)
  x = to_uppercase(lst[0])
  y = column_map.get(lst[1])
  return str(x)+str(y)
def main(a):
    wb = list(a)
    zb = wb[0]+' '+xyt(a)
    return zb
if __name__ == '__main__':
    test = input()
    print(main(test))
