#!/usr/bin/python
import xml.etree.ElementTree as ET

path = 'C:\\Users\\ffayaza\\Documents\\Data\\PROJECT_DATA\\TEST_DATA\\tokenized_data\\dec\\data_03122018.xml'
tree = ET.parse(path)
root = tree.getroot()

file_dir = "C:\\Users\\ffayaza\\Documents\\Data\\PROJECT_DATA\\TEST_DATA\\ex_tok_data\\dec\\data_03122018.xml"
file = open(file_dir, "w", encoding="utf-8")

# list so that we don't mess up the order of iteration when removing items.
iterator = list(root.getiterator('NEWS'))
parent_map = dict((c, p) for p in tree.getiterator() for c in p)
# visited data
visited = set()

for item in iterator:
    title = item.find('TITLE')
    Title_text = title.text
    body = item.find('BODY')
    body_text = body.text
    if Title_text in visited:
        print(Title_text)
        parent_map[item].remove(item)
    else:
        visited.add(Title_text)

for item in root.findall('.//NEWS/*'):
    for news in item:
        news.text.encode('utf8')
i = 1
file.write("<ITEMS>" + "\n")
for item in root:
    item_title = item.find('TITLE').text
    item_body = item.find('BODY').text
    item_url = item.find('LINK').text
    item_date = item.find('DATE').text

    file.write("<NEWS>" + "\n")
    file.write("<INDEX>"+str(i)+"</INDEX>"+"\n")
    file.write("<LINK>"+item_url +"</LINK>"+ "\n")
    file.write("<TITLE>"+item_title +"</TITLE>"+ "\n")
    file.write("<BODY>"+str(item_body) + "</BODY>"+"\n")
    file.write("<DATE>"+item_date +"</DATE>"+ "\n")
    file.write("</NEWS>" + "\n")
    file.write("\n")

    i = i + 1
file.write("</ITEMS>" + "\n")
file.close()
