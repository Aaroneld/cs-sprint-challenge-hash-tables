def has_negatives(a):
    
    corresDict = {}
    returnArr = []

    for num in a:
        if num - (num + num) in a and num > 0:
            corresDict[num] = num

    for num in corresDict.keys():
        returnArr.append(num)

    

    return returnArr


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
