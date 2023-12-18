import json

mydict = {
    'arpit' : "bro"
}

# with open('testdoc.txt', 'w') as filobj:
#     filobj.write(json.dumps(mydict))

filobj = open('testdoc.txt','r')
temp = filobj.read()

mydict = json.loads(temp)
    
print(mydict)