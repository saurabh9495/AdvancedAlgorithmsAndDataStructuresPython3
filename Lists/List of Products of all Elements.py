def find_product(lst):
    # [1,2,3,4]
    left = 1
    right = 1
    product = []
    for i in lst:
        product.append(left)
        left *= i
    for j in range(len(lst)-1,-1,-1):
        product[j] *= right
        right *= lst[j]
    return product

response = find_product([1, 2, 3, 4])
print(response)