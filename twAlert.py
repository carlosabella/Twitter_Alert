import twitterAPI
import twAlertHandler
import emailAPI
import json

tclient = twitterAPI.api
twSendList = []
#Get user lists for alert
# lists for alert, those which last character is "_"
twAccounts = twAlertHandler.getUserLists(tclient,"@abella_carlos")
#twAccounts = json.load(open('alertHelper.json'))
if(twAccounts):
    for jsonStr in twAccounts:
        userList = twAlertHandler.userTwitterTimeline(tclient,jsonStr)
        #userList = twAlertHandler.userTwitterTimeline(tclient,jsonStr['id'])
        if(userList):
           twSendList.append(userList)
for indx,items in enumerate(twSendList):
    content = ""
    for idx, itm in enumerate(items):
        content += items[idx].text + "\r\n \r\n"
    emailAPI.sendEmail(content)