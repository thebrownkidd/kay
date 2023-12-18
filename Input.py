import Automation as at
import Guide as gu
def sel( x ):
#    x = x.lower()
    a = x.split()
    op = a[0]
    if op == "automate" :
        at.auto(a)
    elif op == "guide":
        gu.direct(a)
while 1:
    inp = str(input("Hi, What can I do for you: "))
    if inp == "end" :
        break
    sel(inp)
print("Thanks for using!")
