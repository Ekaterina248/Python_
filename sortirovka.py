print('Быстрая сортировка-------------------------')
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
print(quicksort([10, 5, 2, 15,25,47,47,10,4,5]))

print('Сортировка слиянием--------------------')
def merge_sort(nums):
    if len(nums)>1:
        mid=len(nums)//2
        left=nums[:mid]
        right=nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]<right [j]:
                nums[k]=left[i]
                i +=1
            else:
                nums[k]=right[j]
                j +=1
            k +=1
            print(left, right,k, nums)
        while i<len(left):
            nums[k] =left[i]
            i +=1
            k +=1
        while j<len(right):
            nums[k] =right[j]
            j +=1
            k +=1
        return nums    
list1=[15, 4, 3, 5, 6, 10, 11, 1]   
merge_sort(list1)
print(list1)         


