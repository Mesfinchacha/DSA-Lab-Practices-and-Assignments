arr=[36,18,92,96,10,85,32,23,54,56,55,19]
for i in range (0,len(arr)-1):
        min_element=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min_element]:
                min_element=j
        arr[i],arr[min_element]=arr[min_element],arr[i]
print("Soted array", arr)
