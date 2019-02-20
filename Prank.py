import os
def prank():
    #Step 1 get list names
    listPath = os.listdir(r"C:\Users\rjefferson\ClassProjects\Pics")
    savedPath = os.getcwd()
    print ("The directory it's looking in is " + savedPath)
    os.chdir(r"C:\Users\rjefferson\ClassProjects\Pics")
    #Step 2 Rename files
    for file_name in listPath:
        print ("Old filename is - " + file_name)
        print ("New filename is - " + file_name.translate(None, "0123456789"))
        os.rename(file_name, file_name.translate(None, "0123456789"))

prank()
