import twitterAPI
import twAlertHandler
import emailAPI
import os
from datetime import date

tclient = twitterAPI.api
twSendList = []
#Get user lists for alert
# lists for alert, those which last character is "_" (just first one for now)
twUserMembersLists = twAlertHandler.getUserLists(tclient,os.environ.get('USER_DEFAULT'))
if(twUserMembersLists):
    for twMember in twUserMembersLists:
        memberTimelineList = twAlertHandler.twitterTimeline(tclient,twMember)
        if(memberTimelineList):
           twSendList.append(memberTimelineList)
for indx,items in enumerate(twSendList):
    # Date of email is sent
    date = date.today()
    memberName = items[indx].name
    content = ""
    for itm in items:
        content += itm.created.date().__str__() + ": \n" + itm.text + "\n \n"
    emailAPI.sendEmail(content,date.__str__(), memberName)