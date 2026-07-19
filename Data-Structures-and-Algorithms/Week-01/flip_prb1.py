def sum_two(arr,target):
    note={}
    for i in arr:
        comp=target-arr[i]
        if comp in note:
            return True
        else:
            i=True
    return False
print(sum_two([[2, 7, 11, 15],9]))