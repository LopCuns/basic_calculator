import re

def program():
    operation = input('Enter an operation... \n')
    mult_div = re.findall(r'([-+]?\d+[*/]\d)',operation)
    new_operation = re.sub(r'([-+]?\d+[*/]\d)',"",operation)
    for op in mult_div:
        if '*' in op:
            op_result = str(float(op[0:op.index('*')]) * float(op[-1]))
        else:
            op_result = str(float(op[0:op.index('/')]) / float(op[-1]))  
        new_operation = (op_result,'+' + op_result)[float(op_result) > 0] + new_operation
    print(sum([float(n) for (n,d) in re.findall(r'([+-]?\d+(\.\d)?)',new_operation)]))

program()




