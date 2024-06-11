from Selection_Sort import selectionSort
import math

def bucketSort(customList):
    NumberOfBuckets= round(math.sqrt(len(customList)))
    maxValue=max(customList)
    arr=[]
    for i in range(NumberOfBuckets):
        arr.append([])
    for j in customList:
        index_bucket= math.ceil(j*NumberOfBuckets/maxValue)
        arr[index_bucket-1].append(j)

    for i in range(NumberOfBuckets):
        arr[i]=selectionSort(arr[i])

    k= 0
    for i in range(NumberOfBuckets):
        for j in range(len(arr[i])):
            customList[k]=arr[i][j]
            k+=1
    return customList
customList=[5,8,1,2,9,11,6,12]
print(bucketSort(customList))

    





            












    