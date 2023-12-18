import string as st
import pyperclip as ppc

boilp = {
    "c": '#import<stdio.h>\n#import<conio.h>\nint main(){\n\t\n\nreturn 0;}',
    "C": '#import<stdio.h>\n#import<conio.h>\nint main(){\n\t\n\nreturn 0;}',
    "cpp" : '#include<iostream>\nusing namespace std;\nint mainn(){\n\t\n return 0;}',
    "Cpp" : '#include<iostream>\nusing namespace std;\nint mainn(){\n\t\n return 0;}',
    "c++" : '#include<iostream>\nusing namespace std;\nint mainn(){\n\t\n return 0;}',
    "C++" : '#include<iostream>\nusing namespace std;\nint mainn(){\n\t\n return 0;}',
    "html": '<!DOCTYPE html>\n<html lang="en">\n\t<head>\n\t\t<meta charset="UTF-8">\n\t\t<meta name="viewport" content="width=device-width, initial-scale=1.0">\n\t\t<meta http-equiv="X-UA-Compatible" content="ie=edge">\n\t\t<title>HTML 5 Boilerplate</title>\n\t\t<link rel="stylesheet" href="style.css">\n\t</head>\n\t<body>\n\t\t<script src="index.js"></script>\n\t</body>\n</html>',
    "HTML": '<!DOCTYPE html>\n<html lang="en">\n\t<head>\n\t\t<meta charset="UTF-8">\n\t\t<meta name="viewport" content="width=device-width, initial-scale=1.0">\n\t\t<meta http-equiv="X-UA-Compatible" content="ie=edge">\n\t\t<title>HTML 5 Boilerplate</title>\n\t\t<link rel="stylesheet" href="style.css">\n\t</head>\n\t<body>\n\t\t<script src="index.js"></script>\n\t</body>\n</html>'
    
}

def codehelp(topic):
    match topic:
        case "boilerplate":
            lang = input("Enter language: ")
            lang.lower()
            print("The boilerplate for", lang, " is copied to your clipboard")
            boil = str(boilp[lang])
            print(boil)
            ppc.copy(boil)
def direct(a):
    if a[1] == "code":
        codehelp(a[2])

