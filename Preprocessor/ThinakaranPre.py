#!/usr/bin/python
import xml.etree.ElementTree as ET
from datetime import datetime

# path = "C:\\Users\\ffayaza\\Documents\\MscProject\\Data\\1Week\\16102018\\Thinakaran1.xml"
# tree = ET.parse(path)
# root = tree.getroot()
#
# file = open("C:\\Users\\ffayaza\\Documents\\MscProject\\Data\\PreProcessData\\16102018\\Thinakaran_16102018.xml", "w", encoding="utf-8")
import os

date_var = "03122018"
path = os.path.join('C:\\Users\\ffayaza\\Documents\\MscProject\\Data\\December\\%s\\Thinakaran.xml' % date_var)
tree = ET.parse(path)
root = tree.getroot()
# base dir
_dir = "C:\\Users\\ffayaza\\Documents\\MscProject\\Data\\PreProcessData\\December\\"
# create dynamic name, like "D:\Current Download\Attachment82673"
_dir = os.path.join(_dir, '%s' % date_var)
os.makedirs(_dir, exist_ok=True)
file_dir = os.path.join(_dir, 'Thinakaran_%s.xml' % date_var)
file = open(file_dir,"w", encoding="utf-8")

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
    date = item.find('DATE') or item.find('DATE').find("value")
    print(item.find('DATE').text or item.find('DATE').find("value").text)
    d = datetime.strptime(item.find('DATE').text or item.find('DATE').find("value").text, '%Y-%m-%d %H:%M:%S')
    day_string = d.strftime('%Y-%m-%d')
    # date_text = date
    # print (date)
    # 2018-10-31
    # 2018-11-30
    if "2018-12-03" not in day_string:
        parent_map[item].remove(item)

for item in root.findall('.//item/*'):
    for news in item:
        news.text.encode('utf8')
i = 1
file.write("<ITEMS>" + "\n")
for item in root:
    item_url = item.find('URL').text
    item_title = item.find('TITLE').text or item.find('TITLE').find("value").text
    item_body = item.find('BODY').text.rsplit(' ', 1)[0] or item.find('BODY').find("value").text.rsplit(' ', 1)[0]
    item_date = item.find('DATE').text or item.find('DATE').find("value").text
    print(item_url)
    print(item_title)
    print(item_body)
    print(item_date)
    file.write("<NEWS>" + "\n")
    file.write("<INDEX>"+str(i)+"</INDEX>")
    file.write("\n"+"<LINK>"+item_url +"</LINK>"+ "\n")
    file.write("<TITLE>"+item_title.strip() +"</TITLE>"+ "\n")
    file.write("<BODY>"+item_body.strip() + "</BODY>"+"\n")
    file.write("<DATE>"+str(item_date.strip()[0:10]) +"</DATE>"+ "\n")
    file.write("</NEWS>" + "\n")
    file.write("\n")

    i = i + 1
file.write("</ITEMS>" + "\n")
file.close()
