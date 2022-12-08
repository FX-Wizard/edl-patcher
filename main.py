import os
import re
import linecache


def fixMultipleEDL(fileNames, regexString):
    for fileName in fileNames:
        print(fileName)
        fixEDL(fileName, regexString)

def fixEDL(fileName, regexString) -> None:
    '''
    Fixes EDL file

    Parameters:
    fileName (str) name of file
    regexString (str) regex search pattern, example: VFX_[0-9]{6}_[0-9]{3}
    '''

    with open(fileName, 'r') as file:
        fileData = file.readlines()
        
        for count, line in enumerate(fileData):
            match = re.search(regexString, line)
            if match != None:
                # match.group(0) is the correct word (etc CLSS_101029_500)
                # find line with word needing to be replaced
                replacelineNumber = count - 2
                replaceline = linecache.getline(fileName, replacelineNumber)
                replaceLineWords = replaceline.split()
                ## replaceLineWords[1] (etc A024C025) is the word that needs to be placed
                #get the right content
                fileData[replacelineNumber-1] = replaceline.replace(replaceLineWords[1], match.group(0))

    newFileName = f'{os.path.splitext(fileName)[0]}_fixed.edl'
    with open(newFileName, 'w') as newFile:
        newFile.writelines(fileData)

