from timesheet.timesheet import Timesheet
from mapping.mapping import Mapping
import sys
import os

def main(): 
    filePath, fileName = getFileToProcess('' + sys.argv[1])

    mappingsDict = populateMappings()
    timesheet = processTimesheet(filePath=filePath, mappingsDict=mappingsDict)
    timesheet.createExcel(sys.argv[1] + "\\", fileName.replace(".csv", ".xlsx"))
    print("File " + fileName.replace(".csv", ".xlsx") + " successfully created.")

def processTimesheet(filePath, mappingsDict):
    timesheet = Timesheet()
    timesheet.processTimesheet(filePath)
    timesheet.processEntries(mappingsDict)

    return timesheet

def getFileToProcess(path): 
    dir_list = os.listdir(path)
    filteredList = filterFiles(dir_list)

    index = 1
    for file in filteredList:
        print("(" + str(index) + ") " + file)
        index = index + 1

    var = input("Which file would you like to convert?")

    fileName = filteredList[int(var) - 1]

    return path + "\\" + fileName, fileName

def filterFiles(dirList): 
    filteredList = []
    for file in dirList:
        if ".csv" in file:
            filteredList.append(file)

    return filteredList

def populateMappings():
    mappingsDict = {}
    with open("data\\input\\mappings.txt") as mappingsFile:
        lines = mappingsFile.readlines()
        for line in lines:
            if line[0] != '#':
                lineParts = line.split(',')
                mapping = Mapping(lineParts[1], lineParts[2], strtobool(lineParts[3].strip()))
                mappingsDict[lineParts[0]] = mapping
    return mappingsDict

def strtobool (val):
    val = val.lower()
    if val in ('y', 'yes', 't', 'true', 'on', '1'):
        return True
    elif val in ('n', 'no', 'f', 'false', 'off', '0'):
        return False
    else:
        raise ValueError("invalid truth value %r" % (val,))

main()