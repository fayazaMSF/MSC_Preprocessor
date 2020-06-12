import xml.etree.ElementTree as ET

path = "C:\\Users\\ffayaza\\Documents\\MscProject\\Data\\PreProcessData\\November\\18112018\\Virakesari_18112018.xml"
tree = ET.parse(path)
root = tree.getroot()


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
    if Title_text in visited:
        print("Duplicate Title text : ", Title_text)
        parent_map[item].remove(item)
    # elif "None" in body_text:
    #     print("Body None : ", body_text)
    #     parent_map[item].remove(item)
    else:
        visited.add(Title_text)
tree.write("C:\\Users\\ffayaza\\Documents\\MscProject\\Data\\PreProcessData\\November\\18112018\\Virakesari_181120181.xml", encoding="utf-8")
