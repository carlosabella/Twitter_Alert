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
    date = items[indx].created.date()
    us = items[indx].idName
    content = ""
    for itm in items:
        content += itm.text + "\r\n \r\n"
    emailAPI.sendEmail(content,date, us)