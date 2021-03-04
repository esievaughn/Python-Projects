
import datetime
import pytz                                                 #import pytz for cross platform timezone calculations




                                             
tzPortland = pytz.timezone('America/Los_Angeles')           #pytz pull time zone to return a dateime object with new time zone information
tzNY = pytz.timezone('America/New_York')
tzLondon = pytz.timezone('Europe/London')




def getTime(tzPortland, tzNY, tzLondon):                   #return current time with new time zone information
    currentTime = datetime.datetime.now()
    ctPortland = currentTime.astimezone(tzPortland)
    ctNY = currentTime.astimezone(tzNY)
    ctLondon = currentTime.astimezone(tzLondon)
    return ctPortland, ctNY, ctLondon


def compare(tzPortland, tzNY, tzLondon):
    ctPortland, ctNY, ctLondon = getTime(tzPortland, tzNY, tzLondon)        #assign variables to their current time within function
    branch = {"Portland": ctPortland, "New York": ctNY, "London": ctLondon}
    print("\nOur branches operate from 9:00a.m-5:00p.m in their respective time zones.\n")
    for b in branch:
        o = True
        currentHour = int(branch[b].time().strftime('%H'))                  #time function to determine current time of each branch iteration
        currentTime = branch[b].time().strftime('%H:%M')            
        if currentHour < 9 or currentHour > 17:                             #determine if the current hour is between 9-5, to determine if open
            o = False
        if o:
            print("Our {} branch is currently open. The time there is {}".format(b, currentTime))
        else:
            print("Our {} branch is currently closed. The time there is {}".format(b, currentTime))
            


compare(tzPortland, tzNY, tzLondon)
