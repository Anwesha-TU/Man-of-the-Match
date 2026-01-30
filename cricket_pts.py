def batscore(runs,fours,sixes,balls,field):
    points=(runs/2)+(field*10)
    if runs>=100:
        points+=10
    elif (runs<100) & (runs>=50):
        points+=5
    
    strike_rate=(runs/balls)*100
    if strike_rate>100:
        points+=4
    elif (strike_rate<=100) & (strike_rate>=80):
        points+=2

    points+=fours
    points+=(sixes*2)

    return points

def bowlscore(wkts,runs,overs,field):
    points= (wkts*10)+(field*10)
    if wkts>=5:
        points+=10
    elif (wkts>=3)&(wkts<5):
        points+=5
    
    economy_rate=runs/overs
    if economy_rate<2:
        points+=10
    elif (economy_rate<3.5)&(economy_rate>=2):
        points+=7
    elif (economy_rate<=4.5)&(economy_rate>=3.5):
        points+=4
    
    return points