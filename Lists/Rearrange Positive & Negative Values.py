def rearrange(lst):
    # get negative and positive list after filter and then merge
    return [i for i in lst if i < 0] + [i for i in lst if i >= 0]


print(rearrange([10, -1, 20, 4, 5, -9, -6]))