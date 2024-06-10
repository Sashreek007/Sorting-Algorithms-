def bubbleSort(customList):
    for i in range(len(customList)-1):
        for j in range(len(customList)-1-i):
            if customList[j]>customList[j+1]:
                customList[j],customList[j+1]=customList[j+1],customList[j]
    print(customList)

customList=[5,8,1,2,9,11,6,12]
bubbleSort(customList)









def bubble(customList):
    for i in range(len(customList)-1):
        for j in range(len(customList)-1-i):
            if customList[j]>customList[j+1]:
                customList[j],customList[j+1]=customList[j+1],customList[j]
    print(customList)
bubble(customList)

def selection(customList):
    for i in range(len(customList)):
        minIndex=i
        for j in range(1+i,len(customList)):
            if customList[minIndex]>customList[j]:
                minIndex=j
        customList[minIndex],customList[i]=customList[i],customList[minIndex]
    print(customList)
selection(customList)

def insertionSort(customList):
    for i in range(1,len(customList)):
        key= customList[i]
        j=i-1
        while j>=0 and key<customList[j]:
            customList[j+1]=customList[j]
            j-=1
        customList[j+1]=key
    print(customList)
insertionSort(customList)












