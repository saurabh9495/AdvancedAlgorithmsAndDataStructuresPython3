def merge_lists(lst1, lst2):
    i,j=0,0
    result = []
    while(i < len(lst1) and j < len(lst2)):
        if lst1[i] < lst2[j]:
            result.append(lst1[i])
            i+=1
        elif lst1[i] == lst2[j]:
            result.append(lst1[i])
            result.append(lst2[j])
            i+=1
            j+=1
        else:
            result.append(lst2[j])
            j+=1
    while(i < len(lst1)):
        result.append(lst1[i])
        i+=1
    while(j < len(lst2)):
        result.append(lst2[j])
        j+=1
    return result

response = merge_lists([1, 3, 4, 5],[2, 6, 7, 8])
print(response)