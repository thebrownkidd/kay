import os
def fsearch(file,folder):
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
        
fsearch('FL64.exe','C:\\')