ar.sort()
socksCounter = 0

while len(ar) > 1:
    if ar[0] == ar[1]:
        socksCounter += 1
        ar.pop(0)
            ar.pop(0)
    else:
        ar.pop(0)
            
return socksCounter





def countingValleys(steps, path):
    # Write your code here
    # O(n + (n-1)) --> O(n)
    # O(n + n)
    currentLevel = 0
    stepsList = []
    valleysCount = 0
    for i in range(steps):
        currentLevel += 1 if path[i] == "U" else -1
        stepsList.append(currentLevel)
    
    for i in range(1, len(stepsList)):
        if stepsList[i - 1] == -1 and stepsList[i] == 0:
            valleysCount += 1
            
    return valleysCount