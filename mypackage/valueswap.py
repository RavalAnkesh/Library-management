def swap_with_temp(a, b):
    temp = a
    a = b
    b = temp
    return a, b

    
def swap_with_tuple(a, b):
    a, b = b, a
    return a, b

def swap_with_arithmetic(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b

 
def swap_with_xor(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b


def swap_in_list(lst):
    if len(lst) < 2:
        raise ValueError("List must contain at least two elements.")
    lst[0], lst[1] = lst[1], lst[0]
    return lst

def swap_with_function(x, y):
    return y, x
