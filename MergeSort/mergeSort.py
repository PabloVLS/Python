def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    return merge(sorted_left, sorted_right)



def merge(left, right):
    i=0
    j=0
    c=[]

    while(i< len(left) and j<len(right)):
        if(left[i] < right[j]):
            c.append(left[i])
            i+=1
        else:
            c.append(right[j])
            j+=1
    
    while(i < len(left)):
        c.append(left[i])
        i+=1

    while(j < len(right)):
        c.append(right[j])
        j+=1

    return c

array = [56,84,42,62,14,16,25,26,34,87,92,15,22,45,44]
array1 = merge_sort(array)
print(array1)