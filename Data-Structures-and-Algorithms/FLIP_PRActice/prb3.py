#The Two-Pointer Blueprint
def find(arr,t):
    l=0
    r=len(arr)-1
    while l<r:
        curr=arr[l]+arr[r]
        if curr==t:
            print("yes found it")
            return True
        elif curr>t:
            r=r-1
        else:
            l=l+1
    print("Not found")
    return False
print(find([2, 3, 5, 8, 11],8))
