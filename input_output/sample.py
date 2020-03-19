#input

# Taking integer as an input
# n = int(input())
# print(n)

# Taking string as an input
# s = input()
# print(s)

# a b c
# 1 2 3
# a, b, c = map(int, input().split())
# print(a+b+c)

# a b c d
# 1 2 3 4

# all = [int(i) for i in input().split()]
# List Comprehension
# sum_list = 0
# for i,j in enumerate(all):
#     sum_list += j
# print(sum_list)

# 5 
# 1 3 4 5 6
# n = int(input())
# all = [int(i) for i in input().split()]
# print(all)

# 3 Length of array
# 1
# 3
# 4
# n = int(input())
# tc = []
# for i in range(n):
#     tc.append(int(input()))
# print(tc)

# 2 query
# 3 3 elements
# 12 23 34
# 4 4 elements
# 13 24 35 46


# n = int(input())
# all_n = []
# all_m = []
# for i in range(n): #number of queries
#     m = int(input()) # input size
#     all_n.append(m)
#     all = [int(i) for i in input().split()] #element of list
#     all_m.append(all)
# print(all_n,all_m)


# 4 matrix
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16
# n = int(input())
# for  i in range(n):
#     all = [int(i) for i in input().split()]

#output

# a = [1,2,3,4,5] 
# for i in a:
#     print(i) #Elements printed in different line
#     print(i,end=' ') #Element printed in same line

# a = [1,2,3,4,5]
# for i in range(0,5):
#     print(a[i])

# for i in range(2,11):
#     print(i)

# for i in range(1,10,2):
#     print(i)