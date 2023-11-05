class Debater:
  def __init__(self, name, days, engagementScore):
    self.name = name
    self.days = days
    self.engagementScore = engagementScore

myDebaters = [Debater("Deepanshu", [1,2,3,6,4,5,7], 3),
Debater("Ananya", [6,3,1,5,2,4,7], 7), Debater("Yash", [1,2,3,4,3,6,7], 9),
Debater("Yash2", [1,2,3,4,3,6,7], 8), Debater("Yash3", [1,2,3,4,3,6,7], 6), Debater("Yash4", [1,2,3,4,3,6,7], 5), Debater("Yash5", [1,2,3,4,3,6,7], 4), Debater("Yash6", [1,2,3,4,3,6,7], 3), Debater("Yash7", [1,2,3,4,3,6,7], 10)]

myDays = {"Sunday":0, "Monday":1, "Tuesday":2, "Wednesday":3, "Thursday":4,
"Friday":5, "Saturday":6}

myDebaters.sort(reverse = True, key=lambda Debater: Debater.engagementScore)

def confirmedChecker(debater):
    for i in debater.days:
        if i == 100:
            return True
            break
    return False


def assigner1(myDebaters, myDays):
    layer1Debaters = []
    for day in myDays:
        dayCounter = int(myDays.get(day))
        #print(dayCounter)
        daysDebaters = []
        finalTop1Debaters = []

        for debater in myDebaters:
            #print(confirmedChecker(debater))
            if confirmedChecker(debater)== False and debater.days[dayCounter]==1:
                daysDebaters.append(debater)

        if len(daysDebaters)>=6:
            daysDebaters = daysDebaters[0:5]

        for debater1 in daysDebaters:
            debater1.days[dayCounter] = 100
            finalTop1Debaters.append(debater1)

        layer1Debaters.append(finalTop1Debaters)

    return layer1Debaters


def assigner2(myDebaters, myDays):
    layer2Debaters = assigner1(myDebaters, myDays)
    layer2FinalDebaters = []
    for day in myDays:
        dayCounter = int(myDays.get(day))
        daysDebaters = layer2Debaters[dayCounter]
        finalTop2Debaters = []

        if len(daysDebaters)<6:
            for debater in myDebaters:
                if confirmedChecker(debater)== False and debater.days[dayCounter]==2:
                    daysDebaters.append(debater)
        else:
            continue

        if len(daysDebaters)>=6:
            daysDebaters = daysDebaters[0:5]

        for debater2 in daysDebaters:
            debater2.days[dayCounter] = 100
            finalTop2Debaters.append(debater2)

        layer2FinalDebaters.append(finalTop2Debaters)


    return layer2FinalDebaters

def assigner3(myDebaters, myDays):
    layer3Debaters = assigner2(myDebaters, myDays)
    finalLayer3 = []
    for day in myDays:
        dayCounter = int(myDays.get(day))
        daysDebaters = layer3Debaters[dayCounter]
        finalTop3Debaters = []

        if len(daysDebaters)<6:
            for debater in myDebaters:
                if confirmedChecker(debater)== False and debater.days[dayCounter]==3:
                    daysDebaters.append(debater)
        else:
            continue

        if len(daysDebaters)>=6:
            daysDebaters = daysDebaters[0:5]

        for debater3 in daysDebaters:
            debater3.days[dayCounter] = 100
            finalTop3Debaters.append(debater3.name)

        finalLayer3.append(finalTop3Debaters)

    return finalLayer3

def leaveOutChecker(myDebaters):
    leftOutDebaters = []
    for debater in myDebaters:
        if confirmedChecker(debater)==False:
            leftOutDebaters.append(Debater)
    return leftOutDebaters

print(assigner3(myDebaters, myDays))
print("The unassigned debaters are: "+ str(leaveOutChecker(myDebaters)))
