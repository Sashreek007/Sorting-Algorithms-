

def heapify(customList,n,i):
    smallest=i
    l= i*2 +1
    r= i*2 +2
    if l<n and customList[l]<customList[smallest]:
        smallest=l
    if r<n and customList[r]<customList[smallest]:
        smallest=r
    if smallest!= i:
        customList[i],customList[smallest]=customList[smallest],customList[i]
        heapify(customList,n,smallest)

def heapSort(customList):
    n = len(customList)
    for i in range(int(n/2)-1,-1,-1):
        heapify(customList,n,i)
    for i in range(n-1,0,-1):
        customList[i],customList[0]=customList[0],customList[i]
        heapify(customList,i,0)
    customList.reverse()
    
customList=[8,10,29,38,20,1,2,4,69,35,7]
heapSort(customList)
print(customList)