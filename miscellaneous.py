
lit = [1,2,3,4,5,6,7,8,9,0]
liit = list(filter(lambda n: n%2==0,lit))
print(liit)

list1 = [30, 50, 110, 40, 15, 75]
list2 = [10, 60, 20, 50]

sum_list = [(n1, n2) for n1 in list1 for n2 in list2 if n1 + n2 > 100]

print(sum_list)
