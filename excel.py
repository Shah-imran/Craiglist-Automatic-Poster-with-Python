import xlrd
import pandas as pd
import var
import random
import time

class Excel():
    def __init__(self):
        pass

    def readPva(self, pvaPath):
        data = pd.read_excel (pvaPath, 'Sheet1')
        df = data.to_dict()
        return df

    def readMessage(self, messagePath):
        data = pd.read_excel (messagePath, 'Sheet1')
        df = data.to_dict()
        return df

def main():

    try:
        with open("userPass.txt", "r", encoding="utf-8") as f:
            data = f.read()
            data = data.split(",")
            var.proxyUser = data[0]
            var.proxyPassword = data[1]
            print(var.proxyPassword, var.proxyUser)
    except Exception as e:
        print(e)
    readPva = Excel()
    pvaList = readPva.readPva(var.pvaPath)
    messageList = readPva.readPva(var.messagePath)
    
    l = var.infoLen = len(pvaList["Imap"])

    if var.typeSelect == "activity":
        _temp = "community activity-partners"
    else:
        _temp = "missed-connections"
    messageLen = len(messageList["Title"]) - 1
    for i in range(l):
        tempIndex = random.randint(0, messageLen)
        print(messageLen, tempIndex)
        temp = {
            "clAccount": pvaList["CL Account Login"][i],
            "clEmail": pvaList["CL Email"][i],
            "clPassword": pvaList["CL Password"][i],
            "State": pvaList["State"][i],
            "City": pvaList["City"][i],
            "Zip": pvaList["Zip"][i],
            "Email": pvaList["Email"][i],
            "Password": pvaList["Password"][i],
            "Port": pvaList["Port"][i],
            "Imap": pvaList["Imap"][i],
            "Link": pvaList[_temp][i],
            "title": messageList["Title"][tempIndex],
            "message": messageList["Message"][tempIndex]
        }
        var.info.append(temp.copy())
        var.infoQ.put(temp.copy())
    print(var.info[0])
    var.monitorQ.put('''<p><span style="color: #0C5E3E; font-size: 30px;">{} </span><br>'''.format("Data loading Finshed"))

if __name__ == '__main__':

    readPva = Excel()
    pvaList = readPva.readPva("E:/Suvo/craigslist/pva.xlsx")
    # print(df["Imap"][0])
    messageList = readPva.readPva("E:/Suvo/craigslist/message-1.xlsx")
    # print(df["Title"][0])
    # print(pvaList.keys())
    # print(messageList["Message"][0])
    l = len(pvaList["Imap"])
    if var.typeSelect == "activity":
        _temp = "community activity-partners"
    else:
        _temp = "missed-connections"

    for i in range(l):
        temp = {
            "clAccount": pvaList["CL Account Login"][i],
            "clEmail": pvaList["CL Email"][i],
            "clPassword": pvaList["CL Password"][i],
            "State": pvaList["State"][i],
            "City": pvaList["City"][i],
            "Zip": pvaList["Zip"][i],
            "Email": pvaList["Email"][i],
            "Password": pvaList["Password"][i],
            "Port": pvaList["Port"][i],
            "Imap": pvaList["Imap"][i],
            "Link": pvaList[_temp][i],
            "title": messageList["Title"][i],
            "message": messageList["Message"][i]
        }
        var.info.append(temp.copy())
        var.infoQ.put(temp.copy())

    print(var.info[0].keys())