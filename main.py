import os
import patoolib

#Two empty directories are required
src = "C:/Users/Robert Martini/Desktop/src"
dst = "C:/Users/Robert Martini/Desktop/dst"

#Adds pages from src to dst
def addChapter():
    fileCount = len(os.listdir(src)) #Number of images in src

    #Accounts for other formatting of single digit numbers
    for i in range(fileCount):
        if(i+1<10):
            ind = "0"+str(i+1)
        else:
            ind = str(i+1)

        nextPage = len(os.listdir(dst)) + 1 #Finds new page number by counting ammount of pages in dst
        newSrc = src + "/" + ind + ".JPG" #Src files must be JPG images  and incrementaly numbered starting from 1
        newDst = dst + "/" + str(nextPage) + ".JPG"
        os.rename(newSrc, newDst) #Moves renamed files to dst after incrementing them


#Variables for formating convenience
volNum = 21
chapNum = 182

#Directory name for volumes to extract
volumeDir = "C:/Users/Robert Martini/Desktop/Bleach/Volume " + str(volNum)
rarCount = len(os.listdir(volumeDir)) #Number of rar files in directory

#Extracts rar file into src and executes addChapter() for each file
for i in range(rarCount):
    patoolib.extract_archive(volumeDir + "/" + str(i+chapNum) + ".zip", outdir=src)
    addChapter()
    os.remove(volumeDir + "/" + str(i+chapNum) + ".zip") #Removes rar file after extracted to dst

    fileCount = len(os.listdir(src))

#Moves all files from dst to src
fileCount = len(os.listdir(dst))
for i in range(fileCount):
    dstPage = dst + "/" + str(i+1) + ".JPG"
    volPage = volumeDir + "/" + str(i+1) + ".JPG"
    os.rename(dstPage, volPage)
