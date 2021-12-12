def sort(L):
#for x in L:
    flag = True
    for i in range(len(L)-1):
        #if x > y:
        if L[i] > L[i+1]:
            #switch(x,y)
            nextSpot = L[i+1]
            L[i+1] = L[i]
            L[i] = nextSpot
            flag = False
    if flag:
        return L
    else:
        return sort(L)

def removeXFromList(x, theList):
    #If it's less than 1, just return the list
    if len(theList) < 1:
        return theList

    #If the first thing in the list is what I'm looking for, return everything BUT that
    if theList[0] == x:
        return theList[1:]
    #Only if the first thing in the list is not what I'm looking for,
        #then get the first thing + 1 and retry the function.
    else:
        return [theList[0]] + removeXFromList(x, theList[1:])

print(removeXFromList(3, [1,2,3,4,5,3]))

def sortMax(L):
    if len(L) <= 1:
        return L

    else:
        theMax = max(L)
        return [theMax] + sortMax(removeXFromList(theMax, L))

theList = [1,3,7,3,55,22,30]
print('Sort Max: ', sortMax(theList))
