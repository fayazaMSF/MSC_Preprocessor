#!/usr/bin/python
import xml.etree.ElementTree as ET
import os

date_var = "15122018"
path = os.path.join('C:\\Users\\ffayaza\\Documents\\MscProject\\Data\\December\\%s\\bbc.xml' % date_var)
tree = ET.parse(path)
root = tree.getroot()
# base dir
_dir = "C:\\Users\\ffayaza\\Documents\\MscProject\\Data\\PreProcessData\\December\\"
# create dynamic name, like "D:\Current Download\Attachment82673"
_dir = os.path.join(_dir, '%s' % date_var)
os.makedirs(_dir, exist_ok=True)
file_dir = os.path.join(_dir, 'bbc_%s.xml' % date_var)
file = open(file_dir,"w", encoding="utf-8")
# path = "C:\\Users\\ffayaza\\Documents\\MscProject\\Data\\1Week\\16102018\\bbc.xml"
# tree = ET.parse(path)
# root = tree.getroot()
#
# file = open("C:\\Users\\ffayaza\\Documents\\MscProject\\Data\\PreProcessData\\16102018\\bbc_16102018.xml", "w", encoding="utf-8")
#

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
    # 31 அக்டோபர் 2018
    # 30 நவம்பர் 2018
    if "15 டிசம்பர் 2018" not in date_text:
        parent_map[item].remove(item)

for item in root.findall('.//item/*'):
    for news in item:
        news.text.encode('utf8')
i = 1
file.write("<ITEMS>" + "\n")
for item in root:
    item_url = item.find('URL').text
    item_title = item.find('TITLE').text
    item_body = item.find('BODY').text
    item_date = item.find('DATE').text or item.find('DATE').find("value").text
    print(item_url)
    print(item_title)
    print(item_body)
    print(item_date)
    file.write("<NEWS>"+"\n")
    file.write("<INDEX> "+str(i)+" </INDEX>")
    file.write("\n"+"<LINK> "+item_url +" </LINK>"+ "\n")
    file.write("<TITLE> "+item_title.strip() +" </TITLE>"+ "\n")
    file.write("<BODY> "+item_body.strip() + " </BODY>"+"\n")
    file.write("<DATE> "+str(item_date.strip()) +" </DATE>"+ "\n")
    file.write("</NEWS> "+"\n")
    file.write("\n")

    i = i + 1
file.write("</ITEMS>" + "\n")
file.close()


