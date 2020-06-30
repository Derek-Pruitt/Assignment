import os


def writeData():
    data = '\nHello World!'
    with open('test.txt','a') as f:# a is for append so I can write in the file.
        f.write(data)              # I dont want to use w so it dosent overwrite it.
        f.close


def openFile():
    
                    #Read only
    with open('test.txt','r') as f:
        data = f.read() #calling data f for file
        print(data)     #print()the file
        f.close()       #closing the file so there are no memory leaks


if __name__=="__main__":
    writeData()
    openFile()
