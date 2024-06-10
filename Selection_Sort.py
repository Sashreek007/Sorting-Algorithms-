


def selectionSort(customList):
    for i in range(len(customList)):
        minIndex=i
        for j in range(1+i,len(customList)):
            if customList[minIndex]>customList[j]:
                minIndex=j
        customList[i],customList[minIndex]=customList[minIndex],customList[i]
    return customList




customList=[5,8,1,2,9,11,6,12]
selectionSort(customList)


