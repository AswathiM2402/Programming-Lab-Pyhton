class Time:
    def __init__(self):
        self.__h=int(input("Enter the time in hours:"))
        self.__m=int(input("Enter the time in minutes:"))
        self.__s=int(input("Enter the time in seconds:"))
    def __add__(self,tob2):
        hours=self.__h+tob2.__h
        print("Sum of hours",hours)
        minutes=self.__m+tob2.__m
        print("Sum of minutes",minutes)
       seconds=self.__h+tob2.__h
        print("Sum of seconds",seconds)
        if minutes>=60:
            hours=hours+1
            minutes=minutes-60
        if seconds>=60:
            minutes=minutes+1
            seconds=seconds-60
        return hours,minutes,seconds
print("Enter the time of first object:")
tobj1=Time()
print("Enter the time of second object:")
tobj2=Time()
print("Sum of two time is(Hours,Minutes,Seconds):tobj1+tobj2")
            