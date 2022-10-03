class Time:
    def __init__(self,hours,minutes,seconds): #constructor
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def getHours(self): #accesor hours
        return self.hours
    def getMinutes(self): #accesor minutes
        return self.minutes
    def getSeconds(self): #accesor seconds
        return self.seconds
    def toString(self): #to string
        return (str(self.hours)+":"+str(self.minutes)+":"+str(self.seconds))
    def timeInSeconds(self): #changes the time to second
        return self.hours*60*60 + self.minutes*60 + self.seconds
    def changeTheTime(self,h,m,s): #modify the time
        self.hours = h
        self.minutes = m
        self.seconds = s
    #I have no idea what that will due so some testing probably require
    def twelveHourClock(self): #returns a string with twelve hour time
        noonside = ""
        hours = self.hours
        if self.hours>=12: #if it should be pm set pm
            noonside = "pm"
            if self.hours!=12: #if its not during 12 pm keep hour
                hours -=12
        else: #if should be am
            noonside = "am"
            if self.hours == 0: #if its 12 am set am add 12 to hour
                hours = 12
        return str(hours)+":"+str(self.minutes)+":"+str(self.seconds)+noonside
    def whatTimeIsIt(self): #finds time of day
        if self.hours>=6 and self.hours<12: #morning
            return "morning"
        if self.hours>=12 and self.hours<17: #afternoon
            return "afternoon"
        if self.hours>=17 and self.hours<22: #evening
            return "evening"
        if self.hours>=22 or self.hours<6: #nightime
            return "nighttime"

    def compareTo(self, t): #campares two time objects by time in seconds
        return t.timeInSeconds()-self.timeInSeconds()
    def timeTill(self, t): #finds the time till the time parameter
        hoursTill = 0
        minutesTill = 0
        secondsTill = 0
        if t.hours<self.hours: #next day
            hoursTill = 24 - self.hours + t.hours
        else: #same day
            hoursTill = t.hours - self.hours
        if t.minutes < self.minutes: #next hour
            minutesTill = 60 - self.minutes + t.minutes
            hoursTill-=1
        else: #same hour
            minutesTill = t.minutes - self.minutes
        if t.seconds < self.seconds: #next minute
            secondsTill = 60 - self.seconds+ t.seconds
            minutesTill -= 1
        else: #same minute
            secondsTill = t.seconds - self.seconds
        timeTill = Time(hoursTill,minutesTill,secondsTill)
        return timeTill





