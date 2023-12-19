import subprocess
import os
import string
import webbrowser
import json

filoc = {}
def webop(site):
    webbrowser.open("http://www."+site+".com")
    
def filsearch(file):
    global loc
    global fcount
    fcount = 0 
    obj = open('localloc.txt','r')
    dic = json.loads(obj.read())
    for x in dic.keys():
        if x == file:
            loc = dic[file]
            fcount = 1
            break

def searchop(fil,folder):
        f3 = combsearch(fil,folder)
        f3 = f3.replace("\\","/")
        subprocess.call(f3)
def fsearch(file, folder):
    global f2
    global locat
    f2 = "bruh idk"
    print("Searching in: "+ folder)
    for f in os.listdir(folder):
        try:
            if f2 == file:
                break
            else:
                f2 = f
                if os.path.isfile(folder+f):
                    if f == file:
                        print("\n\nFound it at: "+folder+file+"\n\n")
                        locat = folder+file
                else:
                    fsearch(file,folder+f+"\\")
        except:
            pass

def combsearch (file, folder):
    filsearch(file)
    if fcount != 0:
        return loc
    else:
        fsearch(file, folder)
        obj = open('localloc.txt','r')
        temp = json.loads(obj.read())
        temp[file] = locat
        obj.close()
        obj2 = open('localloc.txt','w')
        obj2.write(json.dumps(temp))
        obj2.close
        return locat
def auto(a):
    if a[1] == "run":
        searchop(a[2]+".exe","C:\\")
    elif a[1] == "visit":
        webop(a[2])
    elif a[1] == "search":
        fsearch(a[2]+".exe","C:\\")