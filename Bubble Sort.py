def bubbleSort(customList):
    for i in range(len(customList)-1):
        for j in range(len(customList)-1-i):
            if customList[j]>customList[j+1]:
                customList[j],customList[j+1]=customList[j+1],customList[j]
    print(customList)

customList=[5,8,1,2,9,11,6,12]
bubbleSort(customList)
















