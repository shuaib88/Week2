#Program takes inputs of initial odometer reading, length of multiple trips,
#gasoline used, and stops when user hits return.



##input: user input interactive thing, asks for two comma seperated values - odometer
##reading and gasoline used. User exits by typing enter(While != "") 
##
##this data is stored in a matrix
##
##program completes matrix operation dividing value of column one by column two
##and storing new values in either the third matrix or a new column in that same
##one
##
##output: maybe use a for loop to iterate through the rows of final matrix
##print ("Leg",i,"used", value from appropriate row,"mpg")




##def multiLegOdom():
##    initialOdom = eval(input("what is your initial odometer reading >> "))
##    count = 0
##    moredata = "yes"
##    distanceList = []
##    gasUsedList = []
##    efficiencyList = []
##    while moredata[0] == "y":
##        tempDist, tempUsed = eval(input("What is your distance travelled and gas used(seperated by comma) >> "))
##        distanceList.append(tempDist)
##        gasUsedList.append(tempUsed)
##        moredata = input("do you have more data? ")
##        print(distanceList)
##    for i in distanceList and j in gasUsedList:
##        tempEffic = i/j
##        efficiencyList.append(tempEffic)
##        print(efficiencyList)
##
##multiLegOdom()

##def main():
##    sum = 0.0
##    count = 0
##    moredata = "yes"
##    while moredata[0] == "y":
##        x = eval(input("enter a number >> "))
##        sum = sum + x
##        count = count + 1
##        moredata = input("do you have more numbers (yes or no)?")
##    print("\nThe average of the numbers is", sum / count)
##
##main()
