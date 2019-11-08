from xml.etree.ElementTree import parse

tree = parse("note.xml")
note = tree.getroot()

print("Depth 3 child")
for parent in note.getiterator("parent"):
    for child in parent.getiterator("child"):
        for grand_child in child.getiterator("grand_child"):
            print(grand_child.text)
