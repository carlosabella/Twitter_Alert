import dbconnection

def getUsMembLastPostInfo():
    userMap = {}
    # This map has as KEY username : membername (username:membername). This is because this method retrieves last twitts from several users
    membLastTwitMap = {}
    cur = dbconnection.conn.cursor()
    #cur.execute("SELECT twmember, lasttwit, u.user FROM public.members m INNER JOIN public.users u ON m.member_id = u.id WHERE u.\"user\" = %s", (memberList,))
    cur.execute("SELECT twmember, lasttwit, u.user, u.email FROM public.members m INNER JOIN public.users u ON m.member_id = u.id")
    rows = cur.fetchall()
    if(rows):        
        for row in rows:
            membLastTwitMap[row['user'] + ":" + row['twmember']] = row['lasttwit']
            #userList.add(row['u.user'])
            if(row['user'] not in userMap):
                userMap[row['user']] = row['email']
        cur.close()
        dbconnection.conn.close()
    return userMap, membLastTwitMap

def updateLastTwitt(membersList):
    cur = dbconnection.conn.cursor()
    for key,value in membersList:
        cur.execute("UPDATE members set = %s lasttwit WHERE twmember = %s",(value, key))    
    dbconnection.conn.commit()
    cur.close()
