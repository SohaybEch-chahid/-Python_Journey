# -----------------------------------------------
# -- File Handling => Write and Append In File --
# -----------------------------------------------

myFile = open(r"D:\Python", "w")
myFile.write("Hello\n")
myFile.write("Third Line")

myFile = open(r"D:\Python\fun.txt", "w")
myFile.write("Elzero Web School\n" * 1000)

myList = ["Oasma\n", "Ahmed\n", "Sayed\n"]

myFile = open(r"D:\Python\s.txt", "w")
myFile.writelines(myList)

myFile = open(r"D:\Python\s.txt", "a")
myFile.write("Elzero")
