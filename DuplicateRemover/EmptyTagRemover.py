import xml.etree.ElementTree as ET

path = "C:\\Users\\ffayaza\\Documents\\DataProcessor\\preprocessor\\ProcessedData\\PreprocessorData\\Sooriyan_FM_News.xml"
tree = ET.parse(path)
root = tree.getroot()


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
    # print("Body text : ", body_text)
    if body_text is None:
        print("Empty Body text : ", body_text)
        parent_map[item].remove(item)
    # elif "None" in body_text:
    #     print("Body None : ", body_text)
    #     parent_map[item].remove(item)
    # else:
    #     visited.add(Title_text)
tree.write("EmptyRemovedSooriyan_FM_News.xml", encoding="utf-8")
