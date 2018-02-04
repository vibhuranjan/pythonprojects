import os
import shutil
import zipfile, time

'''
for folderName, subfolders, filenames in os.walk('C:\\Users\\vibhu.ranjan\\Downloads'):
    print('The current folder is %s' %folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames :
        print('number of files %s' %len(filenames))
        # print('FILES OF ' + folderName + ': ' + filename)
    print('')
'''
sourceDirectory = 'C:\\Users\\vibhu.ranjan\\Downloads'
targetDirectory = 'C:\\fuNke\\docs\\personaldata'
os.chdir(targetDirectory)
readFile = open('read_content.txt','r')
fileSize = 0
for fileContent in readFile.readlines():
    exactFileName = fileContent.split("\n")[0]
    if not exactFileName.__contains__('+'):
        print("'%s ' single word in the file \n" % exactFileName)
        if os.path.isdir(exactFileName):
            print("'%s' directory is already present \n" % exactFileName)
        else:
            os.mkdir(exactFileName)
        fileZip = zipfile.ZipFile('%s.zip' %exactFileName,'w')
        for amerFilename in os.listdir(sourceDirectory):
            if amerFilename.__contains__(fileContent):
                fullPath = os.getcwd() + "\\" + amerFilename
                statinfo = os.stat(amerFilename)
                fileSize = fileSize + statinfo.st_size
                fileZip.write(amerFilename, compress_type=zipfile.ZIP_DEFLATED)
                # os.unlink(fullPath)
                shutil.move('%s.zip' %exactFileName,exactFileName)
        fileZip.close()
    else:
        allWords = exactFileName.split('+')
        zipFileName = '_'
        for count in range(len(allWords)):
            if count == 0:
                zipFileName = allWords[count] + zipFileName
            else:
                zipFileName = zipFileName + '_' + allWords[count]
        secondFileZip = zipfile.ZipFile('%s.zip' % zipFileName, 'a')
        for oneword in allWords:
            for amerFilename in os.listdir(sourceDirectory):
                if amerFilename.__contains__(oneword):
                    os.chdir(sourceDirectory)
                    fullPath = os.getcwd() + "\\" + amerFilename
                    statinfo = os.stat(amerFilename)
                    fileSize = fileSize + statinfo.st_size
                    secondFileZip.write(amerFilename, compress_type=zipfile.ZIP_DEFLATED)
        #os.chdir(targetDirectory)
        #shutil.move('%s.zip' % zipFileName, zipFileName)
        secondFileZip.close()

print(fileSize/1024)
print('End!')
os.chdir(sourceDirectory)
months = ['Feb','Mar','Apr']
for amerFilename in os.listdir(sourceDirectory):
    if amerFilename.__contains__('content'):
        statinfo = os.stat(amerFilename)
        if (time.ctime(statinfo.st_mtime).__contains__('2017') and (time.ctime(statinfo.st_mtime).__contains__('Feb') or
                                                                    time.ctime(statinfo.st_mtime).__contains__('Jan') or
                                                                    time.ctime(statinfo.st_mtime).__contains__('Mar') or
                                                                    time.ctime(statinfo.st_mtime).__contains__('Apr'))):
            print(time.ctime(statinfo.st_mtime))
            print("true")
            os.unlink(amerFilename)
    if (amerFilename.__contains__('apache') and amerFilename.__contains__('zip')) or amerFilename.__contains__('exe') or amerFilename.__contains__('msi'):
        print(time.ctime(os.path.getctime(amerFilename)))
        if not os.path.exists('C:\\EON\\software'+ '\\' + amerFilename):
            shutil.move(sourceDirectory + '\\' + amerFilename,'C:\\EON\\software')
            print('%s file moved to destination path' %amerFilename)
        else:
            print('%s is already present at destination' %amerFilename)
            os.unlink(amerFilename)
            print('extra file deleted!')
    else:
        print('No file present for this condition.')