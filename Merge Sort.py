


def merge(customList,l,m,r):
    n1=m-l+1
    n2=r-m

    L = [0]*n1
    R= [0]*n2
    for i in range(0,n1):
        L[i]=customList[i+l]
    for j in range(0,n2):
        R[j]=customList[m+1+j]
    
    i=0
    j=0
    k=l
    while i<n1 and j<n2:
        if L[i]<R[j]:
            customList[k]=L[i]
            i+=1
        
        else:
            customList[k]=R[j]
            j+=1
        k+=1
    while i<n1:
        customList[k]=L[i]
        i+=1
        k+=1
    while i<n2:
        customList[k]=R[j]
        j+=1
        k+=1 

def mergeSort(customList,l,r):
    if l<r:
        m= (l+(r-1))//2
        mergeSort(customList,l,m)
        mergeSort(customList,m+1,r)
        merge(customList,l,m,r)
        
    return customList
customList=[5,8,1,2,9,11,6,12]
r=len(customList)-1
print(mergeSort(customList,0,7))
    
























