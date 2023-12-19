import subprocess
import os
import string
import webbrowser
import json

filoc = {}
def webop(site):
    webbrowser.open("http://www."+site+".com")
    
def searchop(fil,folder):
        fsearch(fil,folder)
        f3 = locat.replace("\\","/")
        subprocess.call(f3)
# cant use global variables in functions. find a fix
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
def auto(a):
    if a[1] == "run":
        searchop(a[2]+".exe","C:\\")
    elif a[1] == "visit":
        webop(a[2])
    elif a[1] == "search":
        fsearch(a[2]+".exe","C:\\")