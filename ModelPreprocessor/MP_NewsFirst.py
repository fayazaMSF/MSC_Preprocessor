#!/usr/bin/python
import xml.etree.ElementTree as ET

path = 'C:\\Users\\ffayaza\\Documents\\MscProject\\ModelData\\News_First\\2018-09-07T18-38-56.xml'
tree = ET.parse(path)
root = tree.getroot()

file_dir = "C:\\Users\\ffayaza\\Documents\\MscProject\\ModelData\\News_First\\NewsFirst_M.xml"
file_dir_model = "C:\\Users\\ffayaza\\Documents\\MscProject\\ModelData\\News_First\\NewsFirst_Model.txt"
title_dir = "C:\\Users\\ffayaza\\Documents\\MscProject\\ModelData\\News_First\\NewsFirst_title.txt"
body_dir = "C:\\Users\\ffayaza\\Documents\\MscProject\\ModelData\\News_First\\NewsFirst_body.txt"

file = open(file_dir, "w", encoding="utf-8")
fileModel = open(file_dir_model, "w", encoding="utf-8")
titleData = open(title_dir, "w", encoding="utf-8")
bodyData = open(body_dir, "w", encoding="utf-8")

parent_map = dict((c, p) for p in tree.getiterator() for c in p)
# list so that we don't mess up the order of iteration when removing items.
iterator = list(root.getiterator('item'))
# visited data
visited = set()

for item in iterator:
    title = item.find('TITLE')
    Title_text = title.text
    body = item.find('BODY')
    body_text = body.text
    date = item.find('DATE')
    date_text = date.text
    if Title_text in visited:
        print("Duplicate Title text : ", Title_text)
        parent_map[item].remove(item)
        # elif "None" in body_text:
        #     print("Body None : ", body_text)
        #     parent_map[item].remove(item)
    else:
        visited.add(Title_text)

for item in root.findall('.//item/*'):
    for news in item:
        news.text.encode('utf8')
i = 1
file.write("<ITEMS>" + "\n")
for item in root:
    # item_url = item.find('URL').text
    item_title = item.find('TITLE').text
    item_body = item.find('BODY').text
    # item_date = item.find('DATE').text
    # print(item_url)
    # print(item_title)
    # print(item_body)
    # print(item_date)
    file.write("<NEWS>" + "\n")
    # file.write("<INDEX>"+str(i)+"</INDEX>")
    # file.write("\n"+"<LINK>"+item_url +"</LINK>"+ "\n")
    file.write("<TITLE>"+item_title.strip() +"</TITLE>"+ "\n")
    file.write("<BODY>"+item_body.strip() + "</BODY>"+"\n")
    # file.write("<DATE>"+str(item_date.strip()) +"</DATE>"+ "\n")
    file.write("</NEWS> " + "\n")
    file.write("\n")

    fileModel.write(item_title.strip() + "\n")
    fileModel.write(item_body.strip() + "\n")

    titleData.write(item_title.strip() + "\n")

    bodyData.write(item_body.strip() + "\n")


    i = i + 1
file.write("</ITEMS>" + "\n")
file.close()
fileModel.close()
titleData.close()
bodyData.close()
