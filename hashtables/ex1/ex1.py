

def get_indices_of_item_weights(weights, length, limit):

    weightDict = {}
    returnTuple = None

    for i, weight in enumerate(weights):
        if weight in weightDict:
            weightDict[weight].append(i);
        else:
            weightDict[weight] = [i];

    for weight in weightDict.keys():
        if (limit - weight) in weightDict:
            # if weightDictlimit - weight > weight:
            #     returnTuple = (weightDict[limit - weight][0], weightDict[weight][0])
            # else:
            if weight == limit - weight and len(weightDict[weight]) > 1:
                weightDict[weight].sort()
                returnTuple = (weightDict[weight][-1], weightDict[weight][0])
            elif weight != limit - weight:
                if weightDict[weight][0] > weightDict[limit - weight][0]:
                    returnTuple = (weightDict[weight][0], weightDict[limit - weight][0])
                else: 
                    returnTuple = (weightDict[limit - weight][0], weightDict[weight][0])
            break;      

    return returnTuple
