import dbconnection

def getUsMembLastPostInfo():
    # Map with username and email
    userMap = {}
    # This map has as KEY username : membername (username:membername). This is because this method retrieves last twitts from several users
    membLastTwitMap = {}
    cur = dbconnection.conn.cursor()
    # For now, all table is retrieved
    cur.execute("SELECT twmember, lasttwit, u.user, u.email FROM public.members m INNER JOIN public.users u ON m.member_id = u.id")
    rows = cur.fetchall()
    if(rows):        
        for row in rows:
            membLastTwitMap[row['user'] + ":" + row['twmember']] = row['lasttwit']
            if(row['user'] not in userMap):
                userMap[row['user']] = row['email']
        cur.close()
    return userMap, membLastTwitMap

# Update databse with last twitt
def updateLastTwitt(membersList):
    cur = dbconnection.conn.cursor()    
    for key,value in membersList.items():
        cur.execute("UPDATE public.members SET lasttwit = %s WHERE twmember = %s",(value, key))    
    dbconnection.conn.commit()
    cur.close()
    dbconnection.conn.close()