from Time import Time

time1 = Time(12,10,9)
time2 = Time(19,36,20)
time3 = Time(6,5,9)

print(time1.getHours())
print(time1.getMinutes())
print(time1.getSeconds())
print(time1.toString())
print(time1.timeInSeconds())
time2.changeTheTime(17,24,6)
print(time2.toString())
print(time2.twelveHourClock())
print(time1.twelveHourClock())
print(time3.whatTimeIsIt())
print(time2.whatTimeIsIt())
print(str(time1.compareTo(time2)))
print(str(time2.compareTo(time3)))
print(time1.timeTill(time3).toString())
print(time1.timeTill(time2).toString())
print(time2.timeTill(time1).toString())

