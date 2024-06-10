

def insertionSort(customList):
    for i in range(1,len(customList)):
        key=customList[i]
        j=i-1
        while j >= 0 and key < customList[j]:
            customList[j+1]=customList[j]
            j-=1
        customList[j+1]=key
    print(customList)



customList=[5,8,1,2,9,11,6,12]
insertionSort(customList)
























