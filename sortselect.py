def selectsort(list):
 i=0
 n=0
    for (i = 1 to n-1)
        min = i
        for (j = i +1 to n)
            if list[j] < list[min]
            min =j
        if min != i
            swap list[min] and lis[i]




list = [19,2,31,45,6,11,121,27,800,9870,67895,1]
selectsort(list)
print(list)
