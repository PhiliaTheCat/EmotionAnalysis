from encodings import utf_8
from enum import Flag
import jieba 

def is_legal(sample: str):
    if sample == "\n":
        return False
    if sample == "，":
        return False
    if sample == "。":
        return False 
    if (sample == "！"):
        return False
    return True


# open files
fin = open("./外卖评论.csv", "r", encoding = "utf-8")
fout = open("./Partition.txt", "w", encoding = "utf-8")

fin.seek(14, 0)

for each_line in fin:
    cache = each_line.partition(",")
    result = jieba.cut(cache[2])
    for i in result:
        if (not is_legal(i)):
            continue
        fout.write(i + "\n")