
def part1():
    numYears = int(input("Please input the number of years:"))
    pop = 89.2
    for x in range(abs(numYears)):
        if(numYears>0):
         pop = pop + pop * .023
        if(numYears<0):
            pop = pop - pop * .023

    finaldate = 1990 + numYears
    print("The population of Mexico in "+str(finaldate)+" is ")
    print(str(pop)+" million")
def part2():
 startingPop= 89.2
 currentPop = float(input("Enter the population:"))
 currHelp=currentPop
 yearDiff = 0
 if(currentPop > startingPop):
   while currentPop>startingPop:
      startingPop = startingPop*1.023
      yearDiff+=1
 else:
     while(currentPop<startingPop):
         startingPop= startingPop/1.023
         yearDiff-=1
 finalDate = 1990 + yearDiff
 print("Pop in year:"+str(finalDate)+" is equal to ")
 print(str(startingPop))

