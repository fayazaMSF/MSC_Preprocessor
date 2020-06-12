#!/usr/bin/python
import os
import xml.etree.ElementTree as ET
date = "13112018"
# October November December
# _path = os.path.join('C:\\Users\\ffayaza\\Documents\\Data\\PROJECT_DATA\\TEST_DATA\\extracted_data\\December\\%s\\'% date)
# path = os.path.join(_path, 'Virakesari_%s.xml' % date)
path='C:\\Users\\ffayaza\\Documents\\testData\\tokenized\\data_30112018.xml'
    # "C:\\Users\\ffayaza\\Documents\\Data\\PROJECT_DATA\\TEST_DATA\\ex_tok_data\\dec\\data_03122018.xml"
tree = ET.parse(path)
root = tree.getroot()

# _file_dir =("C:\\Users\\ffayaza\\Documents\\Data\\PROJECT_DATA\\TEST_DATA\\formated_data\\December\\%s\\" % date)
# file_dir = os.path.join(_file_dir, 'Virakesari_%s.txt' % date)
# os.makedirs(_file_dir, exist_ok=True)
file_dir="C:\\Users\\ffayaza\\Documents\\Data\\PROJECT_DATA\\TEST_DATA\\Title_Preprocessed_data\\data_30112018.txt"
# C:\\Users\\ffayaza\\Documents\\Data\\PROJECT_DATA\\TEST_DATA\\preprocessed_data\\dec\\data_03122018.txt
file = open(file_dir, "w", encoding="utf-8")

# list so that we don't mess up the order of iteration when removing items.
iterator = list(root.getiterator('NEWS'))

for item in iterator:
    title = item.find('TITLE')
    Title_text = title.text
    body = item.find('BODY')
    body_text = body.text

for item in root.findall('.//NEWS/*'):
    for news in item:
        news.text.encode('utf8')
i = 1
# 107402
# 140605
for item in root:
    item_index = item.find('INDEX').text
    item_title = item.find('TITLE').text
    item_body = item.find('BODY').text
    # file.write(str(item_index)+"\t"+item_title.strip() +" "+ str(item_body) +"\n")
    file.write(str(item_index) + "\t" + item_title.strip() + "\n")
    # i = i + 1
file.close()
