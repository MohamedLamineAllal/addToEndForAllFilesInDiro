from os import *
from os.path import *
import sys
import re

VERBOSE = False


def verbose(msg):
    if(VERBOSE):
        print(msg)


i = 0
# argument control related variable
DIRO_PROVIDED = False
ADD_AFTER_EXTENSION = False
ADD_BEFORE_LAST_EXTENSION = False
ADD_TO_ONLY_NAME_ZERO_EXTENSION = False
ADD_STR_PROVIDED = False
FILES_ONLY = False
# the variable we will work with
diroPath = None
strToAdd = None


for arg in sys.argv:
    if arg == "-f":
        DIRO_PROVIDED = True
        diroPath = sys.argv[i + 1]
    elif arg == "-ad" or arg == "--add":  # searchKeyWord
        ADD_STR_PROVIDED = True
        strToAdd = sys.argv[i + 1]
    elif arg == "-a" or arg == "--afterExt":  # searchKeyWord
        ADD_AFTER_EXTENSION = True
    elif arg == "-b" or arg == "--beforeLastExt":
        ADD_BEFORE_LAST_EXTENSION = True
    elif arg == "-n" or arg == "--nameOnlyNoExt":
        ADD_TO_ONLY_NAME_ZERO_EXTENSION = True
    elif arg == "-v":
        VERBOSE = True
    elif arg == "-fo" or "--fileOnly":
        FILES_ONLY = True
    i += 1

if(not DIRO_PROVIDED):
    diroPath = getcwd()
elif(not isdir(diroPath)):
    diroPath = input(
        "the diro you entred doesn't exist! so please reenter a diro here >")
    while not isdir(diroPath):
        diroPath = input(
            "the diro you entred doesn't exist! so please reenter a diro here >")

if(not ADD_STR_PROVIDED):
    strToAdd = input(
        "you didn't provide what to add! so please enter here what to add >")


argCounter = 0
if(ADD_AFTER_EXTENSION):
    argCounter += 1
if(ADD_BEFORE_LAST_EXTENSION):
    argCounter += 1
if(ADD_TO_ONLY_NAME_ZERO_EXTENSION):
    argCounter += 1

if argCounter > 1 or argCounter == 0:
    msg = ""
    if argCounter == 0:
        msg = "you didn't enter any pattern choice, make one now, enter on of those letters to choose \
        ['a'-> add after extension, 'b' -> add before Last Extension, 'n' -> name Only before any CONSIDRED extension  ]:" 
    else:
        msg = "you entred several choices at once, you can only choose one choice, enter on of those letters to choose \
        ['a'-> add after extension, 'b' -> add before Last Extension, 'n' -> name Only before any CONSIDRED extension  ]"
    answer = input(msg)
    while(answer != 'a' and answer != 'b' and answer != 'n'):
        answer = input(
            "wrong letter! make sure to use one of (a,b,n), enter again your choice:")
    if(answer == 'a'):
        ADD_AFTER_EXTENSION = True
        ADD_BEFORE_LAST_EXTENSION = False
        ADD_TO_ONLY_NAME_ZERO_EXTENSION = False
    elif(answer == 'b'):
        ADD_AFTER_EXTENSION = False
        ADD_BEFORE_LAST_EXTENSION = True
        ADD_TO_ONLY_NAME_ZERO_EXTENSION = False
    else:  # n
        ADD_AFTER_EXTENSION = False
        ADD_BEFORE_LAST_EXTENSION = False
        ADD_TO_ONLY_NAME_ZERO_EXTENSION = True


# operation here
if(ADD_AFTER_EXTENSION):
    currentWorkingDiro = getcwd()
    chdir(diroPath)
    verbose("diroPath chdir to : " + getcwd())
    for num, filename in enumerate(listdir(getcwd()), start=1):
        if(not isfile(filename) and FILES_ONLY):
            continue
        verbose(str(num) + "- fileName : " + filename)
        newFileName = filename + strToAdd
        verbose("newFileName=> " + newFileName)
        verbose("renaming!")
        rename(filename, newFileName)
        verbose("renameDone")
        if(VERBOSE):
            verbose("here the tree of the diro")
            for fname in listdir(getcwd()):
                verbose("--- " + fname)
                verbose("|")
        verbose("")
elif(ADD_BEFORE_LAST_EXTENSION):
    currentWorkingDiro = getcwd()
    chdir(diroPath)
    verbose("diroPath chdir to : " + getcwd())
    for num, filename in enumerate(listdir(getcwd()), start=1):
        if(not isfile(filename) and FILES_ONLY):
            continue
        verbose(str(num) + "- fileName : " + filename)
        beforeLastExtension, lastExtension = splitext(basename(filename))
        newFileName = beforeLastExtension + strToAdd + "." + lastExtension
        verbose("newFileName=> " + newFileName)
        verbose("renaming!")
        rename(filename, newFileName)
        verbose("renameDone")
        if(VERBOSE):
            verbose("here the tree of the diro")
            for fname in listdir(getcwd()):
                verbose("--- " + fname)
                verbose("|")
        verbose("")

else:  # only name
    currentWorkingDiro = getcwd()
    chdir(diroPath)
    verbose("diroPath chdir to : " + getcwd())
    for num, filename in enumerate(listdir(getcwd()), start=1):
        if(not isfile(filename) and FILES_ONLY):
            continue
        verbose(str(num) + "- fileName : " + filename)
        indexOfFirstDot = filename.index('.')
        name = filename[:indexOfFirstDot]
        verbose("name = " + name)
        fullExtension = filename[indexOfFirstDot + 1:]
        verbose("fullExtension = " + fullExtension)
        newFileName = name + strToAdd + "." + fullExtension
        verbose("newFileName=> " + newFileName)
        verbose("renaming!")
        rename(filename, newFileName)
        verbose("renameDone")
        if(VERBOSE):
            verbose("here the tree of the diro")
            for fname in listdir(getcwd()):
                verbose("--- " + fname)
                verbose("|")
        verbose("")

