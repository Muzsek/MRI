import os
import time
from time import gmtime, strftime

localTime = strftime("%A, %Y.%m.%d, %H:%M:%S", gmtime(time.time()))

print("Kérlek add meg a szöveget: ")

szoveg = ""

while(True):
    szoveg1 = input()
    if szoveg1 == "end":
        break
    else:
        szoveg += szoveg1+"\n"

fileName = input("Kérlek add meg a fájl nevét: ")

Path = os.path.join(os.environ["USERPROFILE"],"Desktop","Progprog")

completeName = os.path.join(Path, fileName+".txt")

f = open(completeName, "w")
f.write(localTime+" Bejegyzés: "+"\n"+szoveg)
f.close()
print(szoveg)