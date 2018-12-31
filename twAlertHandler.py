from datetime import date

#Return class
class twInfo:
    def __init___(self,idStr,idName,name,twuser,text, created):
        self.idStr = idStr
        self.idName = idName
        self.name = name
        self.twuser = twuser
        self.text = text
        self.created = created

# Twitter User timeline (20 last)
def twitterTimeline(client, member, lasttw):
    tweetList = []
    tweets = client.user_timeline(member.split(':')[1],since_id=lasttw)
    #tweets = client.user_timeline(member.split(':')[1])
    if(tweets):
        for tweet in tweets:
                twi = type('twInfo', (), {})()
                twi.idName = member.split(':')[1]
                twi.name = tweet.author.name
                twi.twuser = member.split(':')[0]
                twi.idStr = tweet.id_str
                twi.text = tweet.text
                twi.created = tweet.created_at
                tweetList.append(twi)                        
    return tweetList

# this method returns members in the first list with "_" suffix
def getUserLists(client,user):
    usrLst = []
    twlists = client.lists_all(user)
    if(twlists):
        for names in twlists:
            if(names.name.endswith("_")):
                members = client.list_members(user,names.slug)
                if(members):
                    for memb in members:
                        usrLst.append(memb.screen_name)
                break
    return usrLst