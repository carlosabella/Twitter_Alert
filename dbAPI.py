import dbconnection

def getLastPostId():
    userList = set()
    # This map has as KEY username + membername. This is because this method retrieves last twitts from several users
    membLastTwitMap = {}
    cur = dbconnection.conn.cursor()
    #cur.execute("SELECT twmember, lasttwit, u.user FROM public.members m INNER JOIN public.users u ON m.member_id = u.id WHERE u.\"user\" = %s", (memberList,))
    cur.execute("SELECT twmember, lasttwit, u.user FROM public.members m INNER JOIN public.users u ON m.member_id = u.id")
    rows = cur.fetchall()
    if(rows):        
        for row in rows:
            membLastTwitMap[row['u.user'] + row['twmember']] = row['lasttwit']
            userList.add(row['u.user'])
        cur.close()
        dbconnection.conn.close()
    return userList, membLastTwitMap