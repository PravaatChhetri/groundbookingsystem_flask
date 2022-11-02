
def schedule(time):
    t=60*time
    h=0
    m=0
    timeSchedule=['00: 00 AM']
    while h<23:
        if t>=60:
            min=t%60
            h+=(t-min)/60
            if m<60:
                m+=min
            else:
                h+=(m-(m-60))/60
                m=(m%60)
            
            if h<=12:
                if m==60:
                    h+=1
                    m=0
                if m<10:
                    timeSchedule.append(str(int(h))+' : 0'+str(m)+' AM')
                elif h<10:
                    timeSchedule.append('0'+str(int(h))+' : '+str(m)+' AM')
                elif h<10 and m<10:
                    timeSchedule.append('0'+str(int(h))+' : 0'+str(m)+' AM')
                else:
                    timeSchedule.append(str(int(h))+' : '+str(m)+' AM')
            else:
                if m==60:
                    h+=1
                    m=0

                if m<10:
                    timeSchedule.append(str(int(h%12))+' : 0'+str(m)+' PM')
                elif h<10:
                    timeSchedule.append('0'+str(int(h%12))+' : '+str(m)+' PM')
                elif h<10 and m<10:
                    timeSchedule.append('0'+str(int(h%12))+' : 0'+str(m)+' PM')
                else:
                    timeSchedule.append(str(int(h%12))+' : '+str(m)+' PM')        
        else:
            m+=t
    return timeSchedule

def court(r):
    court=[]
    for x in range(1,r):
        court.append("Court "+str(x))
    return court