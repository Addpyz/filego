#v1.1.0 Algorithm simulation
from collections import Counter

def ais(data, b):
    w = []

    # 找到 b 后面的第一个不同元素并添加到 w 中
    i = 0
    while i < len(data) - 1:  # 需要确保不会超出列表范围
        if data[i] == b:
            if data[i + 1] != b:
                w.append(data[i + 1])
            i += 1
        else:
            i += 1
    counter = Counter(w)
    most_common_element, occurrence_count = counter.most_common(1)[0]
    return most_common_element

