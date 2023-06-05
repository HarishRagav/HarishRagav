def sort(array):
    length=len(array)
    if length<2:
        return array
    left=[]
    right=[]
    mid=array[0]
    for i in range(1,length):
        if array[i]<mid:
            left.append(array[i])
        else :
            right.append(array[i])
    leftsort= sort(left)
    rightsort=sort(right)
    return (sort(left)+[mid]+sort(right))

unsorted =[10,9,5,4,7,5,3,2,0]
sorted_array = sort(unsorted)
print(sorted_array)
