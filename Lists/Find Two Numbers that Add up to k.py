def find_sum(lst, k):
    lst.sort()
    st = 0
    end = len(lst)-1
    while(st != end):
        if lst[st]+lst[end] > k:
            end =- 1
        elif lst[st]+lst[end] < k:
            st += 1
        else:
            break
    return [lst[st],lst[end]]

response = find_sum([1, 21, 3, 14, 5, 60, 7, 6],81)
print(response)