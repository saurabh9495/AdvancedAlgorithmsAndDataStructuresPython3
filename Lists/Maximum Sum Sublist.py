def find_max_sum_sublist(lst):
  # [-4,2,-5,1,2,3,6,-5,1]
  if len(lst) < 1:
    return 0
  curr_max = lst[0]
  global_max = lst[0]
  for i in lst:
    if curr_max < 0:
      curr_max = i
    else:
      curr_max += i
    if global_max < curr_max:
      global_max = curr_max
  return global_max