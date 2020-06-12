#!/usr/bin/python
import xml.etree.ElementTree as ET

path = 'C:\\Users\\ffayaza\\Documents\\MscProject\\ModelData\\\Sooriyan_FM_News\\\SooriyanFM.xml'
tree = ET.parse(path)
root = tree.getroot()

file_dir = "C:\\Users\\ffayaza\\Documents\\MscProject\\ModelData\\\Sooriyan_FM_News\\\Sooriyan_FM_News_M.xml"
file = open(file_dir, "w", encoding="utf-8")

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
    date = item.find('DATE').find("value")
    date_text = date.text
    if Title_text in visited:
        print("Duplicate Title text : ", Title_text)
        parent_map[item].remove(item)
        # elif "None" in body_text:
        #     print("Body None : ", body_text)
        #     parent_map[item].remove(item)
    else:
        visited.add(Title_text)
        if body_text.endswith("."):
            print(body_text)
        else:
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
    item_date = item.find('DATE').find("value").text
    print(item_url)
    print(item_title)
    print(item_body)
    print(item_date)
    day, rest = item_date.split(',')
    date, time = rest.split('-')
    file.write("<NEWS>" + "\n")
    file.write("<INDEX>"+str(i)+"</INDEX>")
    file.write("\n"+"<LINK>"+item_url +"</LINK>"+ "\n")
    file.write("<TITLE>"+item_title.strip() +"</TITLE>"+ "\n")
    file.write("<BODY>"+item_body.strip() + "</BODY>"+"\n")
    file.write("<DATE>"+str(date.strip()) +"</DATE>"+ "\n")
    file.write("</NEWS> " + "\n")
    file.write("\n")

    i = i + 1
file.write("</ITEMS>" + "\n")
file.close()
# file1.close()

