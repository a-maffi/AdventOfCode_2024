__register_A = 0
__register_B = 0
__register_C = 0

__pointer = 0


__first_print = True

def inizializza(a,b,c):
    global __register_A
    global __register_B
    global __register_C
    global __pointer
    global __first_print
    __register_A = a
    __register_B = b
    __register_C = c
    __pointer = 0
    __first_print = True

def __value(op):
    if op >= 0 and op <= 3 : return op
    if op == 4 : return __register_A
    if op == 5 : return __register_B
    if op == 6 : return __register_C
    return -1


def __dv(op):
    global __register_A 
    value_op = __value(op)
    numerator = __register_A
    denominator = pow(2,value_op)
    result = numerator // denominator
    return result

def __bxl(op):
    global __register_B
    result = __register_B ^ op
    __register_B = result

def __bst(op):
    global __register_B
    value_op = __value(op)
    result = value_op % 8
    __register_B = result

def __jnz(op):
    global __pointer
    if __register_A != 0:
        __pointer = op - 2

def __bxc(op):
    global __register_B
    global __register_C
    result = __register_B ^ __register_C
    __register_B = result

def __out(op):
    global __first_print
    value_op = __value(op)
    result = value_op % 8
    if(__first_print):
        __first_print = False
    else:
        print(",",end="")
    print(result,end="")

def __adv(op):
    global __register_A
    __register_A = __dv(op)

def __bdv(op):
    global __register_B
    __register_B = __dv(op)

def __cdv(op):
    global __register_C
    __register_C = __dv(op)


COMMANDS=[__adv,__bxl,__bst,__jnz,__bxc,__out,__bdv,__cdv]


def EseguiIstruzione(istruzione,operando):
    global __pointer
    COMMANDS[istruzione](operando)
    __pointer+=2
    return __pointer