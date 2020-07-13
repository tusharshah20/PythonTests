#Problem statement to be updated


#solution to be fixed
def reorderElements(logFileSize, logLines):
    newlog=[]
    newint=[]
    for n in range(logFileSize):
        for i in logLines:
            newlog.append(map(lambda n : n.split()[0,n],i))
        return newlog



