#!/usr/bin/python
import re

file_dir = "C:\\Users\\ffayaza\\Documents\\Data\\all-18-02-07.ta"
file_dir_wr = "C:\\Users\\ffayaza\\Documents\\Data\\all-19-08-27.ta"
file = open(file_dir, "r", encoding="utf-8")
file_w = open(file_dir_wr, "w", encoding="utf-8")
i = 1
for line in file:
    line = re.sub(r'[+?.^$()\[!\]=:{}"",'';|]', '', line)
    print(line)
    file_w.write(line)
    if not line.strip(): continue  # skip the empty line
    # line=line.split(' ', 1)[1]
    
    i = i + 1
file.close()
file_w.close()
# 111440
