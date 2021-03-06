import twitterAPI
import twAlertHandler
import emailAPI
import dbAPI
import os
from datetime import date

tclient = twitterAPI.api
userMap, membLastTwitMap = dbAPI.getUsMembLastPostInfo()

if(userMap and membLastTwitMap):
    twSendList = []
    twUpdateLastTwitt = {}
    for member, lasttw in membLastTwitMap.items():
        memberTimelineList = twAlertHandler.twitterTimeline(tclient,member,lasttw)
        if(memberTimelineList):
            twSendList.append(memberTimelineList)
    if(twSendList):
        for items in twSendList:
            # Date of email is sent
            date = date.today()
            memberName = items[0].name
            toemail = userMap.get(items[0].twuser)
            content = ""        
            twUpdateLastTwitt[items[0].idName] = items[0].idStr
            for i,itm in enumerate(items):
                content += itm.created.date().__str__() + ": \n" + itm.text + "\n \n"
            emailAPI.sendEmail(content,date.__str__(), memberName, toemail)
        if(twUpdateLastTwitt):
            dbAPI.updateLastTwitt(twUpdateLastTwitt)

# function deprecated
#TO-DO delete function
def defaultEmailSend():
    twSendList = []
    #Get user lists for alert
    # lists for alert, those which last character is "_" (just first one for now)
    twUserMembersLists = twAlertHandler.getUserLists(tclient,os.environ.get('USER_DEFAULT'))
    if(twUserMembersLists):
        for twMember in twUserMembersLists:
            memberTimelineList = twAlertHandler.twitterTimeline(tclient,twMember,0)
            if(memberTimelineList):
                twSendList.append(memberTimelineList)
    for indx,items in enumerate(twSendList):
        # Date of email is sent
        date = date.today()
        memberName = items[indx].name
        content = ""
        for itm in items:
            content += itm.created.date().__str__() + ": \n" + itm.text + "\n \n"
        emailAPI.sendEmail(content,date.__str__(), memberName,"")