

def swap(customList,index1,index2):
    customList[index1],customList[index2]=customList[index2],customList[index1]


def pivot(customList,pivotIndex,endIndex):
    swapIndex=pivotIndex
    for i in range(pivotIndex+1,endIndex+1):
        if customList[i]<customList[pivotIndex]:
            swapIndex+=1
            swap(customList,swapIndex,i)
    swap(customList,pivotIndex,swapIndex)
    return swapIndex
def quickSort_helper(customList,left,right):
    if left < right:
        pivot_index= pivot(customList,left,right)
        quickSort_helper(customList,left,pivot_index-1)
        quickSort_helper(customList,pivot_index+1,right)
    return customList
def quickSort(customList):
    return quickSort_helper(customList, 0, len(customList)-1)
customList=[3,5,0,6,1,2,4]

print(quickSort(customList))
    











