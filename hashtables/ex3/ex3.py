def intersection(arrays):
    
    countDict = {}
    interesectList = []

    for i, numList in enumerate(arrays):
        for num in numList:
            if num in countDict:
                if i not in countDict[num]:
                    countDict[num].append(i)
            else:
                countDict[num] = [i]

    for num in countDict.keys():

        interesects = True; 

        for i in range (len(arrays)):
            if i not in countDict[num]:
                interesects = False 

        if interesects:
            interesectList.append(num)



    return interesectList


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
