import twitterAPI
import twAlertHandler
import emailAPI
import json
import os

tclient = twitterAPI.api
twSendList = []
#Get user lists for alert
# lists for alert, those which last character is "_"
twAccounts = twAlertHandler.getUserLists(tclient,os.environ.get('USER_DEFAULT'))

if(twAccounts):
    for twUser in twAccounts:
        userList = twAlertHandler.userTwitterTimeline(tclient,twUser)
        if(userList):
           twSendList.append(userList)
for indx,items in enumerate(twSendList):
    content = ""
    for idx, itm in enumerate(items):
        content += items[idx].text + "\r\n \r\n"
    emailAPI.sendEmail(content)