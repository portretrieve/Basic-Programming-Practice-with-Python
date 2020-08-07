
# Importing the copyfile function from Shutil Module

from shutil import copyfile

#Asking user the input for source as well as destination

sourceFile = input("Please enter the file name that you want to copy content from : ")

destinationFile = input("Please enter the file name that you want to copy the content into : ")

#Using Copyfile function to copy content of Source file into Destination file

copyfile(sourceFile, destinationFile)

print("\n")


#Opening and reading the contents of Destination file

openedFile = open(destinationFile)
print(openedFile.read())
openedFile.close()
