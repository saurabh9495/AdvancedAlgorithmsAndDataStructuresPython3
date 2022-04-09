from unittest import result

ops = ["5","2",'C','D','+']
result = None
ops_result = []
record = []
for i in ops:
    if i == '+':
        updated_score = record[-1]+record[-2]
        record.append(updated_score)
        print(record)
    elif i == 'D':
        updated_score_ = ops_result[-1]*ops_result[-2]
        record.append(updated_score_)
        print(record)
    elif i == 'C':
        record.pop()
        print(record)
    else:
        ops_result.append(int(i))
        record.append(int(i))
        print(record)
result = sum(record)
print(result)