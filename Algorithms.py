import re
import const

#Checks the input is format of "N,N,N,N,..,N"
#return False if it is not correct
#return True if it is correct
def inputChecker(inputText,InvalidInputText,screen):
    checker = re.search(r"[0-9]+(,[0-9]+)*", inputText) #Regex Function
    if (checker == None) or (checker.group()!=inputText):
        #If it is none there is no match. (checker == None)
        #If matched case is not the same with input text, that means it is invalid. (checker.group()!=inputText)
        InvalidInputText.draw(screen)
        return False
    return True

#This function is to set heights of bars
#Also, it is drawing
#Note: It is returning True if size is proper
def arrayHeightSetter(barArray,inputArray,InvalidInputText,screen):
    resetAllBars(barArray,screen)                                           #Firstly, reset the bars
    if len(barArray) < len(inputArray):                                     #Compare the length of input and number of bars
        InvalidInputText.draw(screen)                                       #Invalid Input !! is printed
        return False
    maxValue=max([int(i) for i in inputArray])                              #Take the maximum value of input Array
    for ind,val in enumerate(inputArray):
        color=const.rectangleColor                                          #Set the default color                                                      
        newHeight=float(int(val)*const.maksHeightBar)/(maxValue)            #Set the height according to biggest bar
        barArray[ind].updateHeight(newHeight)                               #Update Height
        barArray[ind].changeColor(color)                                    #Make it visible
        barArray[ind].addText(inputArray[ind])                              #Add text
        barArray[ind].draw(screen)                                          #Draw
    return True

#Reseting all bars we have
def resetAllBars(barArray,screen):
    for i in barArray:
        i.delete(screen)        
        i.clearAll(screen)

#Highlight order setter
#returns the order list
def highlightOrder(inputArrayOrg):
    highlightlist=[]                                    #init the list
    inputArray=[int(i) for i in inputArrayOrg]          #init an array to store sorting
    #Apply the Bubble sorted algorithm
    fixedElement=0  #The number of sorted elements in the algorithm
    while fixedElement!=len(inputArray):
        for ind in range(0, len(inputArray)-fixedElement-1):       
            highlightlist.append([[ind,ind+1],[]])          #Make i
            if inputArray[ind]>inputArray[ind+1]:
                inputArray[ind],inputArray[ind+1] = inputArray[ind+1],inputArray[ind]
                highlightlist.append([[],[ind,ind+1]])
        fixedElement+=1
        highlightlist.append([-1])
    return highlightlist

#Bars is going to be changed in the given index, ind1 and ind2. 
def barsChangeDraw(ind1,ind2,barArray,inputArray,invalidInputText,screen):
    inputArray[ind1],inputArray[ind2]=inputArray[ind2],inputArray[ind1] #Update array
    arrayHeightSetter(barArray,inputArray,invalidInputText,screen) #Call the again height setter to apply changes on the screen