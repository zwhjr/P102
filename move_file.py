import os
import shutil

from_dir = "C:/Users/zahme_85berv3/downloads"
to_dir = "C:/Users/zahme_85berv3/downloads/di"

listOfFiles = os.listdir(from_dir)
#print(listOfFiles)

for i in listOfFiles:
    name, extension = os.path.splitext(i)
    #print(name)
    #print(extension)
    if extension == "":
        continue
    if extension in [".txt", ".doc", ".docx", ".pdf"]:
        path1 = from_dir + "/" + i
        path2 = to_dir + "/" + "docsFile"
        path3 = to_dir + "/" + "docsFile" + "/" + i

        if os.path.exists(path2):
            print("Moving" + i + "...")
            shutil.move(path1, path3)

        else:
            os.makedirs(path2)
            print("Moving" + i + "...")
            shutil.move(path1, path3)