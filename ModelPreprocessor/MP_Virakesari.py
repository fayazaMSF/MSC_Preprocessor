#!/usr/bin/python
import xml.etree.ElementTree as ET
import os

path ='C:\\Users\\ffayaza\\Documents\\MscProject\\ModelData\\Virakesari\\Virakesari.xml'
    # "C:\\Users\\ffayaza\\Documents\\MscProject\\ModelData\\Virakesari\\Virakesari_M4.xml"

tree = ET.parse(path)
root = tree.getroot()

file_dir ="C:\\Users\\ffayaza\\Documents\Data\\DATA_MODEL\\data\\Virakesari.xml"
    # "C:\\Users\\ffayaza\\Documents\\MscProject\\ModelData\\Virakesari\\Virakesari_M5.xml"
# file_dir_model = "C:\\Users\\ffayaza\\Documents\\MscProject\\ModelData\\Virakesari\\Virakesari_Model2.xml"
file = open(file_dir, "w", encoding="utf-8")
# fileModel = open(file_dir_model, "w", encoding="utf-8")
parent_map = dict((c, p) for p in tree.getiterator() for c in p)

# list so that we don't mess up the order of iteration when removing items.
iterator = list(root.getiterator('NEWS'))
# visited data
visited = set()

for item in iterator:
    title = item.find('TITLE')
    Title_text = title.text
    body = item.find('BODY')
    body_text = body.text
    # date = item.find('DATE')
    # date_text = date.text
    if Title_text in visited:
        # print("Duplicate Title text : ", Title_text)
        parent_map[item].remove(item)
        # elif "None" in body_text:
        #     print("Body None : ", body_text)
        #     parent_map[item].remove(item)
    else:
        # visited.add(Title_text)
        # if '.' in str(body_text):
            print(body_text)
        # else:
        #     parent_map[item].remove(item)


for item in root.findall('.//NEWS/*'):
    for news in item:
        news.text.encode('utf8')
i = 1
file.write("<ITEMS>" + "\n")
for item in root:
    # item_url = item.find('URL').text
    item_title = item.find('TITLE').text
    item_body = item.find('BODY').text
    if '...' in str(item_body):
        print(item_body)
        item_body = item.find('BODY').text.rsplit(' ', 1)[0]
    else:
        item_body = item.find('BODY').text
    # .rsplit(' ', 1)[0]
    # item_date = item.find('DATE').text
    # print(item_url)
    # print(item_title)
    # print(item_body)
    # # print(item_date)
    file.write("<NEWS>")
    # file.write("<INDEX>"+str(i)+"</INDEX>")
    # file.write("\n"+"<LINK>"+item_url +"</LINK>"+ "\n")
    file.write("<TITLE>"+item_title +"</TITLE>"+ "\n")
    file.write("<BODY>"+item_body + "</BODY>")
    # fileModel.write(item_title.strip() + "\n")
    # fileModel.write(item_body.strip())
    # file.write("<DATE>"+str(item_date.strip()[0:10]) +"</DATE>"+ "\n")
    file.write("</NEWS>" + "\n")
    file.write("\n")

    i = i + 1
file.write("</ITEMS>" + "\n")
file.close()
# fileModel.close()
