import subprocess
import os
import string
import webbrowser
import json

filoc = {}
def webop(site):
    webbrowser.open("http://www."+site+".com")
    
def searchop(fil,folder):
    global f2
    global f3
    f2 = "aa sun"
    try:
        for f in os.listdir(folder):
            print(folder+f)
            if f2 == (fil+".exe"):
                break    
            else:
                f2 = f
                if os.path.isfile(folder + f):
                    if f == (fil + ".exe"):
                        print("milgya " + folder + f)
                        f3 = folder + f
                        f3 = f3.replace("\\","/")
                        subprocess.call(f3)
                    else:
                        searchop(fil,folder + f + "\\")
    except:
        pass

def fsearch(file, folder):
    global f2
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
                else:
                    fsearch(file,folder+f+"\\")
        except:
            pass
def auto(a):
    if a[1] == "run":
        searchop(a[2],"C:\\")
    elif a[1] == "visit":
        webop(a[2])
    elif a[1] == "search":
        fsearch(a[2],"C:\\")