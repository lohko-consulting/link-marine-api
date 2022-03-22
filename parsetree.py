import json

def parseFile():
    f = open("merkle.tree","r")
    tree ={}
    for line in f:
        lineArray = line.split(" ")
        if lineArray[0] == 'Parent(concatenation':
            tree[lineArray[6]] = lineArray[10]
        else:
            tree[lineArray[3]] = lineArray[7]
    return tree

print("Parsing tree")
tree = parseFile()
print("Tree parsed")
with open('merkletree.json', 'w') as convert_file:
     convert_file.write(json.dumps(tree))