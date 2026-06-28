# -------------------------------------
# -- File Handling => Important Info --
# -------------------------------------

import os

myFile = open(r"D:\Python\s.txt", "a")
myFile.truncate(5)

myFile = open(r"D:\Python\s.txt", "a")
print(myFile.tell())

myFile = open(r"D:\Python\s.txt", "r")
myFile.seek(11)
print(myFile.read())

os.remove(r"D:\Python\s.txt")
