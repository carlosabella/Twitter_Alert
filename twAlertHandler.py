# Return class
class twInfo:
        def __init___(self,idStr,idName,text):
                self.idStr = idStr
                self.idName = idName
                self.text = text

# Twitter User timeline (20 last)
def userTwitterTimeline(client, user):
        tweetList = []
        tweets = client.user_timeline(user)
        if(tweets):
                for tweet in tweets:
                        twi = type('twInfo', (), {})()
                        twi.idName = user
                        twi.idStr = tweet.id_str
                        twi.text = tweet.text
                        tweetList.append(twi)                                
        return tweetList

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
        return usrLst